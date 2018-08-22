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
              Object.keys(words).forEach(w => articles += '<div class ="panel">' + `${w}: occured ${words[w]["occurences"]} times in lyrics. Here is a related article ` + '<div class="panel-heading"> <h3 class="panel-title">' + `<a href=${words[w]["url"]}> ${words[w]["title"]} </a>` + '</h3> </div></div>'  )
              $('#articles').html(articles);
            }

            function load_top_words(query) {
                $.ajax({
                    url: 'articles',
                    data: {'query': query},
                    dataType: 'json',
                    type: 'GET',
                    success: function(data) {
                        //console.log(format_chart(data));
                        build_chart(data);
                        build_articles(data);
                    }
                });
            }

