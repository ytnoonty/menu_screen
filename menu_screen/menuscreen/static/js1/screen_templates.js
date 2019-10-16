class ScreenTemplate {
  constructor () {

  }


  updateDisplayScreenArtistTime(data, eventData, settings) {
    // console.log(settings);
    let data0116 = data.slice(0,16);
    let data1722 = data.slice(16,22);
    let data0108 = data.slice(0,8);
    let data0816 = data.slice(8,16);
    let example6 = document.getElementById('example6');
    let example6HTML = '';
    // console.log(eventData);
    example6HTML = `
    <div class="row mt-3">
      <div class="col-lg">
        <div class="list-group">
          <ul class="list-group-flush list-group-bts">`;
            data0108.forEach(function(beer){
              example6HTML += `
              <li class="cardvs">
                <table class="beer-screen-table">
                  <tr class="beer-screen-tr">
                    <h1 class="italic-font bold-font txt-clr-ylw left-spacer no-btm-margin"><span class="">${beer.name}</span></h1>
                  </tr>
                  <tr class="left-spacer beer-screen-tr font-sml">
                    <td class=" w-third">${beer.style}</td>
                    <td class="w-fifth"><span class="font-xxsml"></span> ${beer.abv}<span class="font-xsml">%</span></td>
                    <td class="italic-font  w-third">${beer.brewery}</td>
                  </tr>
                </table>
              </li>`
            });
    example6HTML += `
          </ul>
        </div>
      </div>
      <div class="col-lg">
        <div class="list-group">
          <ul class="list-group-flush list-group-bts">
              <li class="cardvs backgrounds">
                <table>
                  <tr>
                    <h1 class="text-center italic-font bold-font txt-clr-ylw left-spacer no-btm-margin"><span class="events-heading">EVENTS OF THE DAY</span></h1>
                  </tr>
                  <tr class="beer-screen-tr event-details">
                    <h3 class="text-center bold-font">March ${new Date().getDate()}th ${new Date().getFullYear()}</h3>
                  </tr>
                </table>
              </li>
          </ul>
        </div>
        <div class="list-group">
          <ul class="list-group-flush list-group-bts">`;
            eventData.forEach(function(event){
              let etoe = event.time_of_event;
              etoe = etoe.split(':');
              let etoeHour = parseInt(etoe[0]);
              let etoeMin = parseInt(etoe[1]);
              if (etoeHour > 0 && etoeHour < 13) {
                // console.log(`${etoeHour}:${etoeMin} AM`);
              } else {
                etoeHour -= 12;
                // console.log(`${etoeHour}:${etoeMin} PM`);
              }

              example6HTML += `
              <li class="cardvs backgrounds">
                <table>
                  <tr>
                    <td><h1 class="italic-font bold-font txt-clr-ylw left-spacer no-btm-margin"><span class="event-artist">${event.artist}</span></h1></td>
                    <td><h1 class="italic-font bold-font left-spacer no-btm-margin><span class="event-details">${event.time_of_event}</span></h1></td>
                  </tr>
                </table>
              </li>`
            });
    example6HTML += `
          </ul>
        </div>
      </div>
    </div>`;
    if (example6 !== null) {
      example6HTML += `<div></div>`;
      example6.innerHTML = example6HTML;
      let backgrounds = document.querySelectorAll('.backgrounds');
      // console.log(backgrounds);
      let eventsHeading = document.querySelector('.events-heading');
      let eventArtist = document.querySelectorAll('.event-artist');
      let eventDetails = document.querySelectorAll('.event-details');
      eventsHeading.style.color = `${settings.font_color}`;
      eventArtist.forEach(eArtist => {
        eArtist.style.color = `${settings.font_color}`;
        eArtist.style.fontSize = `${settings.nameFontSize.font_sizes}`;
      });
      eventDetails.forEach(eventDetail => {
        eventDetail.style.fontSize = `${settings.abvIbuFontSize.font_sizes}`;
      });
      backgrounds.forEach(background => {
        background.style.backgroundImage = `linear-gradient(to bottom, #333, ${settings.background_color})`;
      });
    }
    ///////////////////////////////////////////////
    // END  UPDATE
    ///////////////////////////////////////////////
  }


  updateDisplayScreen(data, eventData, settings) {
    // console.log(settings);
    let data0116 = data.slice(0,16);
    let data1722 = data.slice(16,22);
    let data0108 = data.slice(0,8);
    let data0816 = data.slice(8,16);
    let example6 = document.getElementById('example6');
    let example6HTML = '';
    // console.log(eventData);
    example6HTML = `
    <div class="row mt-3">
      <div class="col-lg">
        <div class="list-group">

          <div class="list-group">
            <ul class="list-group-flush list-group-bts">
                <li class="cardvs card-bottom-margin-5vh backgrounds">
                  <table>
                    <tr>
                      <h1 class="text-center italic-font bold-font txt-clr-ylw left-spacer no-btm-margin"><span class="events-heading">DRAFT BEERS OF THE WEEKEND</span></h1>
                    </tr>
                  </table>
                </li>
            </ul>
          </div>



          <ul class="list-group-flush list-group-bts">`;
            data0108.forEach(function(beer){
              // example6HTML += `
              // <li class="cardvs">
              //   <table class="beer-screen-table">
              //     <tr class="beer-screen-tr">
              //       <h1 class="italic-font bold-font txt-clr-ylw left-spacer no-btm-margin"><span class="">${beer.name}</span></h1>
              //     </tr>
              //     <tr class="left-spacer beer-screen-tr font-sml">
              //       <td class=" w-third">${beer.style}</td>
              //       <td class="w-fifth"><span class="font-xxsml"></span> ${beer.abv}<span class="font-xsml">%</span></td>
              //       <td class="italic-font  w-third">${beer.brewery}</td>
              //     </tr>
              //   </table>
              // </li>`
              example6HTML += `
              <li class="cardvs card-9vh">
                <table class="beer-screen-table">
                  <tr class="beer-screen-tr">
                    <h1 class="italic-font bold-font txt-clr-ylw left-spacer no-btm-margin">
                      <span class="beer-name event-artist">${beer.name}</span>
                      <span class="beer-style"> - ${beer.style}</span>
                    </h1>
                  </tr>
                </table>
              </li>`
            });
    example6HTML += `
          </ul>
        </div>
      </div>
      <div class="col-lg">




        <div class="list-group">
          <ul class="list-group-flush list-group-bts">
              <li class="cardvs backgrounds">
                <table>
                  <tr>
                    <h1 class="text-center italic-font bold-font txt-clr-ylw left-spacer no-btm-margin"><span class="events-heading">EVENTS OF THE DAY</span></h1>
                  </tr>
                  <tr class="beer-screen-tr event-details">
                    <h3 class="text-center bold-font">March ${new Date().getDate()}th ${new Date().getFullYear()}</h3>
                  </tr>
                </table>
              </li>
          </ul>
        </div>


        <div class="list-group">
          <ul class="list-group-flush list-group-bts">`;



            example6HTML += `
            <li class="card-bottom-margin-5vh backgrounds">
              <table>
                <tr>
                  <h1 class="text-center italic-font bold-font txt-clr-ylw left-spacer no-btm-margin"><span class="events-heading"> - Now Playing - </span></h1>
                </tr>
              </table>
            </li>`;

            eventData.forEach(function(event){
              let eventStartMonth = parseInt(event.date_of_event.split("-")[1]);
              let eventStartDate = parseInt(event.date_of_event.split("-")[2]);
              let eventStartHour = event.time_of_event.split(":")[0];
              let eventStartMin = event.time_of_event.split(":")[1];
              let eventEndHour = event.endtime_of_event.split(":")[0];
              let eventEndMin = event.endtime_of_event.split(":")[1];
              let currentHour = new Date().getHours();
              let currentMin = new Date().getMinutes();

              let eventStartDateTime = new Date(new Date().getFullYear(), eventStartMonth - 1, eventStartDate, eventStartHour, eventStartMin, 0, 0);
              let eventEndDateTime = new Date(new Date().getFullYear(), eventStartMonth - 1, eventStartDate, eventEndHour, eventEndMin, 0, 0);
              let currentDateTime = new Date();
              let eventStartTime;

              // console.log(eventStartDateTime.valueOf());
              // console.log(eventEndDateTime.valueOf());
              // console.log(currentDateTime.valueOf());
              // console.log(eventStartDateTime);
              // console.log(eventEndDateTime);
              // console.log(currentDateTime);
              //
              //
              // console.log('^^^^^^^^^^^^^ TIME LOGGING ^^^^^^^^^^^^^^');
              // console.log(`new Date(): ${new Date()}`);
              // console.log(`eventStartDateTime: ${eventStartDateTime}`);
              // console.log(`currentHour: ${currentHour}, currentMin: ${currentMin}`);
              // console.log(`eventStartHour: ${eventStartHour}, eventStartMin: ${eventStartMin}`);
              // console.log(`eventEndHour: ${eventEndHour}, eventEndMin: ${eventEndMin}`);
              // console.log('^^^^^^^^^^^^^ TIME LOGGING ^^^^^^^^^^^^^^');

              if ( currentDateTime.valueOf() > eventStartDateTime.valueOf() && currentDateTime.valueOf() < eventEndDateTime.valueOf() ) {

                    // example6HTML += `
                    // <li class="cardvs card-vh-control backgrounds">
                      // <table>
                      // <tr>
                        // <h1 class="italic-font bold-font txt-clr-ylw left-spacer no-btm-margin"><span class="event-artist">${event.artist}</span></h1>
                      // </tr>
                      // <tr class="left-spacer beer-screen-tr font-sml event-details">
                        // <td class="bold-font w-third">${event.location}</td>
                        // <td class="italic-font bold-font w-third">${eventStartHour}:${eventStartMin}</td>
                        // <td class="w-fifth mr-"><span class="font-xxsml"></span> ${event.date_of_event}<span class="font-xsml"></span></td>
                      // </tr>
                    // </table>
                    // </li>`;

                    if (eventStartHour >= 12) {
                      eventStartHour = Math.abs(eventStartHour - 12);
                      eventStartTime = (`${eventStartHour}:${eventStartMin}pm`);
                    } else if (eventStartHour < 1) {
                      eventStartHour = 12;
                      eventStartTime = (`${eventStartHour}:${eventStartMin}am`);
                    } else {
                      eventStartTime = (`${eventStartHour}:${eventStartMin}am`);
                    }

                    example6HTML += `
                      <li id="now-playing" class="cardvs card-9vh backgrounds">
                        <table>
                          <tr>
                            <h1 class="italic-font bold-font txt-clr-ylw left-spacer no-btm-margin">
                              <span class="event-artist">${event.artist}  </span>
                              <span class="italic-font event-time">${eventStartTime} - </span>
                              <span class="event-location">${event.location}</span>
                            </h1>
                          </tr>
                        </table>
                      </li>`;

              }
            });

            example6HTML += `
              <li class=" card-bottom-margin-5vh backgrounds">
                <table>
                  <tr>
                    <h1 class="text-center italic-font bold-font txt-clr-ylw left-spacer no-btm-margin"><span class="events-heading"> - On Stage Soon - </span></h1>
                  </tr>
                </table>
              </li>`;
            eventData.forEach(function(event){
              let eventStartMonth = parseInt(event.date_of_event.split("-")[1]);
              let eventStartDate = parseInt(event.date_of_event.split("-")[2]);
              let eventStartHour = event.time_of_event.split(":")[0];
              let eventStartMin = event.time_of_event.split(":")[1];
              let eventEndHour = event.endtime_of_event.split(":")[0];
              let eventEndMin = event.endtime_of_event.split(":")[1];
              let currentMonth = new Date().getMonth() + 1;
              let currentDate = new Date().getDate();
              let currentHour = new Date().getHours();
              let currentMin = new Date().getMinutes();

              let eventStartDateTime = new Date(new Date().getFullYear(), eventStartMonth - 1, eventStartDate, eventStartHour, eventStartMin, 0, 0);
              let eventEndDateTime = new Date(new Date().getFullYear(), eventStartMonth - 1, eventStartDate, eventEndHour, eventEndMin, 0, 0);
              let currentDateTime = new Date();
              let eventStartTime;

              if (eventStartMonth == currentMonth) {
                if (eventStartDate == currentDate) {
                  if ( currentDateTime.valueOf() <= eventStartDateTime.valueOf() ) {
                    //       console.log('^^^^^^^^^^^^^ON STAGE SOON^^^^^^^^^^^^^^');
                    //       console.log(`currentHour: ${currentHour}, currentMin: ${currentMin}`);
                    //       console.log(`eventStartHour: ${eventStartHour}, eventStartMin: ${eventStartMin}`);
                    //       console.log(`eventEndHour: ${eventEndHour}, eventEndMin: ${eventEndMin}`);
                    //       console.log('^^^^^^^^^^^^^ON STAGE SOON^^^^^^^^^^^^^^');

                    // example6HTML += `
                    // <li class="cardvs card-vh-control backgrounds">
                    //   <table>
                    //     <tr>
                    //       <h1 class="italic-font bold-font txt-clr-ylw left-spacer no-btm-margin"><span class="event-artist">${event.artist}</span></h1>
                    //     </tr>
                    //     <tr class="left-spacer beer-screen-tr font-sml event-details">
                    //       <td class="bold-font w-third">${event.location}</td>
                    //       <td class="italic-font bold-font w-third">${eventStartHour}:${eventStartMin}</td>
                    //       <td class="w-fifth mr-"><span class="font-xxsml"></span> ${event.date_of_event}<span class="font-xsml"></span></td>
                    //     </tr>
                    //   </table>
                    // </li>`;
                    if (eventStartHour >= 12) {
                      eventStartHour = Math.abs(eventStartHour - 12);
                      eventStartTime = (`${eventStartHour}:${eventStartMin}pm`);
                    } else if (eventStartHour < 1) {
                      eventStartHour = 12;
                      eventStartTime = (`${eventStartHour}:${eventStartMin}am`);
                    } else {
                      eventStartTime = (`${eventStartHour}:${eventStartMin}am`);
                    }

                    example6HTML += `
                      <li class="cardvs card-vh-control backgrounds">
                        <table>
                          <tr>
                            <h1 class="italic-font bold-font txt-clr-ylw left-spacer no-btm-margin">
                              <span class="event-artist">${event.artist}  </span>
                              <span class="italic-font bold-font w-third">${eventStartTime}</span>
                              <span class="bold-font w-third"> - ${event.location}</span>
                            </h1>
                          </tr>
                        </table>
                      </li>`;
                  }
                }
              }
            });


    example6HTML += `
          </ul>
        </div>
      </div>
    </div>`;
    if (example6 !== null) {
      example6HTML += `<div></div>`;
      example6.innerHTML = example6HTML;

      let nowPlayingColor = document.querySelector('#now-playing');

      let beerNames = document.querySelectorAll('.beer-name');
      let beerStyle = document.querySelectorAll('.beer-style');
      let backgrounds = document.querySelectorAll('.backgrounds');
      // console.log(backgrounds);
      let eventsHeadings = document.querySelectorAll('.events-heading');
      let eventArtist = document.querySelectorAll('.event-artist');
      let eventTimes = document.querySelectorAll('.event-time');
      let eventLocations = document.querySelectorAll('.event-location');
      let eventDetails = document.querySelectorAll('.event-details');


      beerNames.forEach(names => {
        names.style.fontSize = `${settings.nameFontSize.font_sizes}`;
      });
      beerStyle.forEach(styles => {
        styles.style.fontSize = `${settings.abvIbuFontSize.font_sizes}`;
      });
      eventsHeadings.forEach(eventsHeading => {
        eventsHeading.style.color = `${settings.font_color}`;
      });
      eventArtist.forEach(eArtist => {
        eArtist.style.color = `${settings.font_color}`;
        eArtist.style.fontSize = `${settings.nameFontSize.font_sizes}`;
      });
      eventTimes.forEach(time => {
        time.style.fontSize = `${settings.abvIbuFontSize.font_sizes}`;
      });
      eventLocations.forEach(location => {
        location.style.fontSize = `${settings.abvIbuFontSize.font_sizes}`;
      });
      eventDetails.forEach(eventDetail => {
        eventDetail.style.fontSize = `${settings.abvIbuFontSize.font_sizes}`;
      });
      backgrounds.forEach(background => {
        background.style.backgroundImage = `linear-gradient(to bottom, #333, ${settings.background_color})`;
      });
      // nowPlayingColor.style.backgroundImage = `linear-gradient(to bottom, ${settings.background_color}, #fff, ${settings.background_color})`;
      nowPlayingColor.style.backgroundImage = `linear-gradient(to bottom, #fff, ${settings.background_color})`;
    }
    ///////////////////////////////////////////////
    // END  UPDATE
    ///////////////////////////////////////////////
  }
  // //////////////////////////////////////////////////////
  // // END ASYNC AWAIT updateExample6()
  // //////////////////////////////////////////////////////



  //////////////////////////////////////////////////////
  // START EASY AJAX.JS updateExample6()
  //////////////////////////////////////////////////////

  updateExample6() {
    const http = new easyHTTP;

    // Create POST
    http.postRecieve('/update', function(err, post) {
      // console.log('************NEW POST BEGIN postRecieve***************');
      if (err) {
        console.log(err);
      } else {
        exampleSix(post);
      }
    }); // END function http.postRecieve()
  } // END FUNCTION updateExample6()




  //////////////////////////////////////////////////////
  // END EASY AJAX.JS updateExample6()
  //////////////////////////////////////////////////////
  exampleSix(data, settings) {
    // console.log("WHAT IS IN THE POST VAR: " + data);
    // console.log('**********NEW POST END OF NEW POST REQUEST**********');
    // console.log("NEW POST this.responseText: " + data);
      // data = JSON.parse(data);
    // console.log('data: ' + data);
    // console.log('******************NEW POST  END OF PARSING JSON DATA *****************');
      let data0116 = data.slice(0,16);
      let data1722 = data.slice(16,22);
      let data0108 = data.slice(0,8);
      let data0816 = data.slice(8,16);
    // console.log("data0116: " + data0116);
    // console.log('data0116[0]: ' + data0116[0].name, data0116[0].style);
    // console.log('data0116[1]: ' + data0116[1].name, data0116[1].style);
    // console.log('******************NEW POST  END OF DATA0116 *****************');
    // console.log('******************NEW POST  END postRecieve *****************');
    ///////////////////////////////////////////////
    // START  UPDATE
    ///////////////////////////////////////////////
    let example6 = document.getElementById('example6');
    let example6HTML = '';
    example6HTML = `
    <div class="row mt-3">
      <div class="col-lg">
        <div class="list-group">
          <ul class="list-group-flush list-group-bts">`;
            data0108.forEach(function(beer){
              example6HTML += `
              <li class="cardvs">
                <table class="beer-screen-table">
                  <tr class="beer-screen-tr">
                    <h1 class="italic-font bold-font txt-clr-ylw left-spacer no-btm-margin"><span class="">${beer.name}</span></h1>
                  </tr>
                  <tr class="left-spacer beer-screen-tr font-sml">
                    <td class=" w-third">${beer.style}</td>
                    <td class="w-fifth"><span class="font-xxsml"></span> ${beer.abv}<span class="font-xsml">%</span></td>
                    <td class="italic-font  w-third">${beer.brewery}</td>
                  </tr>
                </table>
              </li>`
            });
    example6HTML += `
          </ul>
        </div>
      </div>
      <div class="col-lg">
        <div class="list-group">
          <ul class="list-group-flush list-group-bts">`;
            data0816.forEach(function(beer){
              example6HTML += `
              <li class="cardvs">
                <table>
                  <tr>
                    <h1 class="italic-font bold-font txt-clr-ylw left-spacer no-btm-margin"><span class="">${beer.name}</span></h1>
                  </tr>
                  <tr class="left-spacer beer-screen-tr font-sml">
                    <td class="bold-font w-third">${beer.style}</td>
                    <td class="w-fifth"><span class="font-xxsml"></span> ${beer.abv}<span class="font-xsml">%</span></td>
                    <td class="italic-font bold-font w-third">${beer.brewery}</td>
                  </tr>
                </table>
              </li>`
            });
    example6HTML += `
          </ul>
        </div>
      </div>
    </div>`;
    if (example6 !== null) {
      // console.log(example6HTML);
      //USED FOR TESTING THE ajax update
      //uncomment line below and reload browser or reboot pi
      example6HTML += `<div></div>`;
      example6.innerHTML = example6HTML;
    }
    // console.log(example6HTML);
    ///////////////////////////////////////////////
    // END  UPDATE EXAMPLE6
    ///////////////////////////////////////////////
  }

  twoColNameAbv (data, settings) {
    // console.log("WHAT IS IN THE POST VAR: " + data);
    // console.log('**********NEW POST END OF NEW POST REQUEST**********');
    // console.log("NEW POST this.responseText: " + data);
      // data = JSON.parse(data);
    // console.log('data: ' + data);
    // console.log('******************NEW POST  END OF PARSING JSON DATA *****************');
      let data0116 = data.slice(0,16);
      let data1722 = data.slice(16,22);
      let data0108 = data.slice(0,8);
      let data0816 = data.slice(8,16);
    // console.log("data0116: " + data0116);
    // console.log('data0116[0]: ' + data0116[0].name, data0116[0].style);
    // console.log('data0116[1]: ' + data0116[1].name, data0116[1].style);
    // console.log('******************NEW POST  END OF DATA0116 *****************');
    // console.log('******************NEW POST  END postRecieve *****************');
    ///////////////////////////////////////////////
    // START  UPDATE
    ///////////////////////////////////////////////
    let example6 = document.getElementById('example6');
    let example6HTML = '';
    example6HTML = `
    <div class="row mt-3">
      <div class="col-lg">
        <div class="list-group">
          <ul class="list-group-flush list-group-bts">`;
            data0108.forEach(function(beer){
              example6HTML += `
              <li class="cardvs">
                <table class="beer-screen-table">
                  <tr class="beer-screen-tr">
                    <h1 class="italic-font bold-font txt-clr-ylw left-spacer no-btm-margin"><span class="">${beer.name}</span></h1>
                  </tr>
                  <tr class="left-spacer beer-screen-tr font-sml">
                    <td class=" w-third">${beer.style}</td>
                    <td class="w-fifth"><span class="font-xxsml"></span> ${beer.abv}<span class="font-xsml">%</span></td>

                  </tr>
                </table>
              </li>`
            });
    example6HTML += `
          </ul>
        </div>
      </div>
      <div class="col-lg">
        <div class="list-group">
          <ul class="list-group-flush list-group-bts">`;
            data0816.forEach(function(beer){
              example6HTML += `
              <li class="cardvs">
                <table>
                  <tr>
                    <h1 class="italic-font bold-font txt-clr-ylw left-spacer no-btm-margin"><span class="">${beer.name}</span></h1>
                  </tr>
                  <tr class="left-spacer beer-screen-tr font-sml">
                    <td class="bold-font w-third">${beer.style}</td>
                    <td class="w-fifth"><span class="font-xxsml"></span> ${beer.abv}<span class="font-xsml">%</span></td>

                  </tr>
                </table>
              </li>`
            });
    example6HTML += `
          </ul>
        </div>
      </div>
    </div>`;
    if (example6 !== null) {
      // console.log(example6HTML);
      //USED FOR TESTING THE ajax update
      //uncomment line below and reload browser or reboot pi
      example6HTML += `<div></div>`;
      example6.innerHTML = example6HTML;
    }
    // console.log(example6HTML);
    ///////////////////////////////////////////////
    // END  UPDATE
    ///////////////////////////////////////////////
  }
}
