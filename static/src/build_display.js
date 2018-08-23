/*
===========================================================================================
Helpers ->  build articles | builds chart
===========================================================================================
*/

           function format_chart(data) {
              var formatted = [] ;
              Object.keys(data['data']).forEach(key => formatted.push([key, data.data[key]["percentages"] ]) );
              return formatted;
            }

            function build_chart(data) {
              Highcharts.chart('chart', {
                        chart: {
                          plotBackgroundColor: null,
                          plotBorderWidth: 0,
                          plotShadow: false
                        },
                        title: {
                          text: 'Top Words<br>In Lyrics',
                          align: 'center',
                          verticalAlign: 'middle',
                          y: 40
                        },
                        tooltip: {
                          pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
                        },
                        plotOptions: {
                          pie: {
                            dataLabels: {
                              enabled: true,
                              distance: -50,
                              style: {
                                fontWeight: 'bold',
                                color: 'white'
                              }
                            },
                            startAngle: -90,
                            endAngle: 90,
                            center: ['50%', '75%']
                          }
                        },
                        series: [{
                          type: 'pie',
                          name: 'Occurences',
                          innerSize: '50%',
                          data: format_chart(data)
                        }]
              });
            }

            function build_articles(data) {
              words = data.data
              var articles = '<div>';
              Object.keys(words).forEach(w => articles += '<div class ="panel">' + `${w}: occured ${words[w]["occurences"]} times in lyrics. Here is a related article ` + '<div class="panel-heading"> <h6 class="panel-title">' + `<a href=${words[w]["url"]}> ${words[w]["title"]} </a>` + '</h3> </div></div>'  )
              $('#articles').html(articles);
            }

/*
===========================================================================================
Ajax to Server-side lyric analyzer
===========================================================================================
*/
            function load_top_words(lyrics, key) {
                var data;
                data = (key === "spotify" ? {"spotify": JSON.stringify(lyrics)} : {"query": lyrics}) ;
                $.ajax({
                    url: 'articles',
                    data: data,
                    dataType: 'json',
                    type: 'GET',
                    success: function(data) {
                        //console.log(format_chart(data));
                        build_chart(data);
                        build_articles(data);
                        console.log('Dope now hook up charts');
                        console.log(data);
                    }
                });
            }
/*
===========================================================================================
Spotify Component
===========================================================================================
*/

function request_authorization() {
                $('#login-button').click( function() {
                    var client_id = '7a848f3295c047b08e6e118c2121acbf';
                    var redirect_uri = 'http://localhost:5000/'; //'https://lyric-analyzer.herokuapp.com/'
                    var scope = 'user-read-private user-read-email user-top-read';
                    var url = 'https://accounts.spotify.com/authorize';
                    url += '?response_type=token';
                    url += '&client_id=' + encodeURIComponent(client_id);
                    url += '&scope=' + encodeURIComponent(scope);
                    url += '&redirect_uri=' + encodeURIComponent(redirect_uri);
                    //url += '&state=' + encodeURIComponent(state);
                    window.location = url;
                });
            }

            function getHashParams() {
                /*
                  * Obtains parameters from the hash of the URL
                  * @return Object
                */
                var hashParams = {};
                var e, r = /([^&;=]+)=?([^&;]*)/g,
                            q = window.location.hash.substring(1);
                while ( e = r.exec(q)) {
                    hashParams[e[1]] = decodeURIComponent(e[2]);
                }
                return hashParams;
            }

            function get_access_token() {
                var params =  getHashParams();
                var access_token = params.access_token ;
                return access_token;
            }

            function verify_access_token(is_a_token) {
                if (is_a_token) {
                    //call_spotify(is_a_token);
                    return true;
                }
            }

            function build_billboard(data) {
                var songs = data;
                var billboard = `<table class="table table-striped table-sm table-bordered table-dark" style="min-width: 310px; height: 100px; max-width: 300px; margin: 0 auto">
                                   <thead class="thead-light">
                                     <tr class="rounded">
                                      <th scope="col">#</th>
                                      <th scope="col">Artist</th>
                                      <th scope="col">Track</th>
                                    </tr>
                                   </thead>
                                   <tbody>`

                songs.slice(0,10).forEach((s,ind) => billboard += `<tr class='clickable-row'>
                                                       <th scope="row">${ind+1}</th>
                                                       <td>${s.artist}</td>
                                                       <td>${s.name}</td>
                                                       </tr>`)
                billboard += `</tbody> </table>`
                $('#billboard').html(billboard)
                //songs.forEach(s => billboard += `<div> artist ${s.artist} : song ${s.name} </div>`)
               $(".clickable-row").click(function() {
                  var out = [];
                  var $row = $(this).closest("tr"), // Finds the closest row <tr>
                   $tds = $row.find("td"); // Finds all children <td> elements
                  $.each($tds, function() {  // Visits every single <td> element
                    out.push($(this).text()) // Get the text within the <td>
                  });
                  var info;
                  out.map(function() {
                    info =  {"artist": out[0], "track": out[1]}
                    return
                  })
                  console.log(out);
                  console.log(info);
                  load_top_words(info, "spotify");
               });
            }

            function call_spotify(a_t) {
                $.ajax({
                   url: 'https://api.spotify.com/v1/me/top/tracks',
                   headers: {
                       'Authorization': 'Bearer ' + a_t
                   },
                   success: function(response) {
                       console.log('playlist');
                       console.log(response);
                       var songs = [];
                       var tracks = response.items
                       tracks.forEach(t => songs.push({"name": t.name, "artist": t.artists[0].name}))
                       console.log(songs);
                       build_billboard(songs);
                       $('#login').hide()
                   }
                });
            }

            function spotify_implicit_grant_flow() {
                request_authorization();
                var access_token = get_access_token();
                var verified = verify_access_token(access_token);
                if (verified === true) call_spotify(access_token);
            }

/*
===========================================================================================
User input Component
===========================================================================================
*/

function user_input() {
    $('#user-input').click(function() {
       var lyrics = $('#query').val();
       load_top_words(lyrics, "query")
    });
}

