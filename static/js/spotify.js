            function request_authorization() {
                $('#login-button').click( function() {
                    var client_id = '7a848f3295c047b08e6e118c2121acbf';
                    var redirect_uri = 'http://localhost:5000/';
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
                   }
                });
            }

            function spotify_implicit_grant_flow() {
                request_authorization();
                var access_token = get_access_token();
                var verified = verify_access_token(access_token);
                if (verified === true) call_spotify(access_token);
            }

