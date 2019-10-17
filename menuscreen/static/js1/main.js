// Init ScreenUpdater
const screen = new ScreenUpdater;
const screenTemplate = new ScreenTemplate;

let flashMsgDiv = document.getElementById('flash-msg-div');
let updateProcessPrint = document.getElementById('update-tv-screen');
let refreshed = false;
let refreshCount = 0;

let form = document.getElementById('edit_form');
let editList = document.getElementById('edit-beerlist');

let editWinelistForm = document.getElementById('edit-winelist-form');
let editWinelistBtn = document.getElementById('edit-winelist-btn');

// flash message dissapear after 2.5seconds
setTimeout(() => {
  flashMsgDiv.style.display = 'none';
}, 2500);

if (editWinelistBtn != null) {
  editWinelistBtn.addEventListener("click", function(e) {
    editWinelistForm.submit();
  });
}

// adds click to refresh on the shamrocks jacks logo on beer_tv_screen
if (updateProcessPrint != null) {
  updateProcessPrint.addEventListener('click', function(e){
    window.location.reload();
    updateScreens();
    // moveTheStuff();
  });
}
let divTicker = document.querySelector(".ticker");
let infoTicker = document.querySelectorAll(".info");
// let movement = getMovement(infoTicker);
// let duration = getDuration(infoTicker);
let oldMovement = 0;

if (editList != null) {
  editList.addEventListener("click", function(e) {
    form.submit();
    // e.preventDefault();
  });
  // updateScreens();
}

///////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////
// BEGIN LOGIN FORM FOR STORAGE
///////////////////////////////////////////////////////////////////////////////
let loginForm = document.querySelector("#login-form");
let loginFormSubmitBtn = document.querySelector("#login-form-submit-button");
let loginUsername = document.querySelector("#login-username");
let loginPassword = document.querySelector("#login-password");
let stayLoggedIn = document.querySelector("#stay-check");
if (loginForm !== null) {
  console.log("login");
  loginUsername.value = "HELLO There";
  loginPassword.value = "PASSWORD";
  loginFormSubmitBtn.addEventListener("click", e => {
    console.log("CLICKING LOGIN NOW");
    if (stayLoggedIn.checked) {
      if (stayLoggedIn.value == "true"){
        console.log("THIS IS IT");
        console.log(stayLoggedIn.value);
      }
    }
    loginForm.submit();
    e.preventDefault();
  });
}
///////////////////////////////////////////////////////////////////////////////
// END LOGIN FORM FOR STORAGE
///////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////


// if (divTicker) {
//   animateTicker(divTicker, movement, duration);
// }

// moveTheStuff();
// getMovement();
// getDuration();
updateExample6();
updateScreens();
function updateScreens() {
  movement = getMovement(infoTicker);
  duration = getDuration(infoTicker);
  // console.log("oldMovement: " + oldMovement);
  // console.log("oldMovement: " + oldMovement + "   movement: " + movement)
  if (oldMovement != movement) {
    oldMovement = movement;
    // console.log("oldMovement in the IF: " + oldMovement);
    if (divTicker != null) {
      animateTicker(divTicker, movement, duration);
    }
  }
  // console.log("*************UPDATING SCREENS*************");
  loadBeerlist();
  updateProccess_print();
  updateBottleBeers();
  updateOnTapCurrent();
  updateOnTapNext();
  updateExample6();
  loadTicker();
  screenRefresh();
  setTimeout(updateScreens, 2000);
}

//////////////////////////////////////////////////////
// START screenRefresh()
//////////////////////////////////////////////////////
function screenRefresh() {
  // console.log("***********Screen Refresh************")
  let currentTime = new Date();
  let hour = currentTime.getHours();
  let min = currentTime.getMinutes();
  let sec = currentTime.getSeconds();
  let millSec = currentTime.getMilliseconds();
  if ((sec > 48 && sec < 60)){
    refreshed = true;
    // console.log("hour: " + hour + "  min: " + min + "  sec: " + sec + "     refreshed: " + refreshed);
  }
  if ((hour == 2 || hour == 11 || hour == 14 || hour == 23) && min == 1 && (sec >= 0 && sec < 12) && refreshed == true) {
    refreshCount++;
    refreshed = !refreshed;
    window.location.reload();
  }
}
//////////////////////////////////////////////////////
// END screenRefresh()
//////////////////////////////////////////////////////



//////////////////////////////////////////////////////
// START loadBeerlist()
//////////////////////////////////////////////////////
function loadBeerlist(e) {
  // console.log('*************TESTING loadBeerlist*************');
  const xhr = new XMLHttpRequest();
  // console.log('READYSTATE1', xhr.readyState);
  // Open
  xhr.open('POST', '/update', true);
  // console.log('READYSTATE2', xhr.readyState);
  // console.log('STATUS before onload', this.status);
  // xhr.onload
  xhr.onload = function() {
    // console.log('READYSTATE-3', xhr.readyState);
    // console.log('STATUS after onload: ', this.status);
    if (this.status === 200) {
      // console.log(this.responseText);
      let data = JSON.parse(this.responseText);
      let data0116 = data.slice(0,16);
      let data1722 = data.slice(16,22);
      let data0108 = data.slice(0,8);
      let data0816 = data.slice(8,16);
      ///////////////////////////////////////////////
      // START BEERS_PRINT.HTML UPDATE
      ///////////////////////////////////////////////
      let beerListDivBP = document.getElementsByClassName('beer-list-div-bp');
      // console.log(beerListDiv);
      let htmlStuffBP = '';
      htmlStuffBP += `<ul id="" class='list-group-flush'>`;
      data0116.forEach(function(beer){
        htmlStuffBP += `<li id="" class='list-group-item'>${beer.id_dropdown}.  <span class="larger-text txt-clr-grn">${beer.name}</span> - ${beer.style} - ${beer.abv}% ABV - ${beer.ibu} IBU - ${beer.location} - <span class="italic-font">${beer.brewery}</span></li>`;
      });
      htmlStuffBP += `</ul>`;
      if (beerListDivBP[0] !== undefined) {
        beerListDivBP[0].innerHTML = htmlStuffBP;
      }
      let monthPBP = document.getElementsByClassName('month-p-bp');
      if (monthPBP[0] !== undefined) {
        monthPBP[0].innerHTML = `<span class="mx-3 larger-text txt-clr-grn">${data1722[0].name}</span>`;
      }
      let comingsoonPBP = document.getElementById('comingsoon-p-bp');
      if (comingsoonPBP !== null) {
        comingsoonPBP.innerHTML = `
        <span class="mx-4 larger-text txt-clr-grn">${data1722[1].name}</span>
        <span class="mx-4 larger-text txt-clr-grn">${data1722[2].name}</span>
        <span class="mx-4 larger-text txt-clr-grn">${data1722[3].name}</span>
        <span class="mx-4 larger-text txt-clr-grn">${data1722[4].name}</span>
        <span class="mx-4 larger-text txt-clr-grn">${data1722[5].name}</span>
        `;
      }
      ///////////////////////////////////////////////
      // END BEERS_PRINT.HTML UPDATE
      ///////////////////////////////////////////////
    }
  }
  xhr.send();
  // e.preventDefault();
}
//////////////////////////////////////////////////////
// END loadBeerlist()
//////////////////////////////////////////////////////

//////////////////////////////////////////////////////
// START updateProccess_print(e) UPDATE
//////////////////////////////////////////////////////
function updateProccess_print(e) {
  // console.log('*************TESTING updateProccess_print*************');
  const xhr = new XMLHttpRequest();
  // console.log('READYSTATE1', xhr.readyState);
  // Open
  xhr.open('POST', '/update', true);
  // console.log('READYSTATE2', xhr.readyState);
  // console.log('STATUS before onload', this.status);
  // xhr.onload
  xhr.onload = function() {
    // console.log('READYSTATE-3', xhr.readyState);
    // console.log('STATUS after onload: ', this.status);
    if (this.status === 200) {
      // console.log(this.responseText);
      let data = JSON.parse(this.responseText);
      let data0116 = data.slice(0,16);
      let data1722 = data.slice(16,22);
      let data0108 = data.slice(0,8);
      let data0816 = data.slice(8,16);
      ///////////////////////////////////////////////
      // START proccess_print.html UPDATE
      ///////////////////////////////////////////////
      let beerListDivPP = document.getElementsByClassName('beer-list-div-pp');
      // beerListDivPP[0].innerHTML = "";
      // console.log(beerListDivPP[0]);
      let htmlStuffPP = '';
      htmlStuffPP += `<ul id="" class='beer-list-loop-pp list-group-flush'>`;
      data0116.forEach(function(beer){
        htmlStuffPP += `<li id="" class='list-group-item-pp list-group-item'>${beer.id_dropdown}.  <span class="larger-text txt-clr-grn">${beer.name}</span> - <span class="bold-font italic-font">${beer.style}</span> - ${beer.abv}% ABV - ${beer.ibu} IBU - ${beer.location} - <span class="italic-font">${beer.brewery}</span></li>`;
      });
      htmlStuffPP += `</ul>`;
      if (beerListDivPP[0] !== undefined) {
        beerListDivPP[0].innerHTML = htmlStuffPP;
      }
      let monthPPP = document.getElementsByClassName('month-p-pp');
      if (monthPPP[0] !== undefined) {
        monthPPP[0].innerHTML = `<span class="mx-3 larger-text txt-clr-grn">${data1722[0].name}</span> - <span class="bold-font italic-font">${data1722[0].style}</span>`;
      }
      let comingsoonPPP = document.getElementById('comingsoon-p-pp');
      if (comingsoonPPP !== null) {
        // console.log(comingsoonPPP);
        comingsoonPPP.innerHTML = `
        <span class="mx-4 larger-text txt-clr-grn">${data1722[1].name}</span>
        <span class="mx-4 larger-text txt-clr-grn">${data1722[2].name}</span>
        <span class="mx-4 larger-text txt-clr-grn">${data1722[3].name}</span>
        <span class="mx-4 larger-text txt-clr-grn">${data1722[4].name}</span>
        `;
        // comingsoonPPP.innerHTML = "";
      }
      ///////////////////////////////////////////////
      // END proccess_print.html UPDATE
      ///////////////////////////////////////////////
    }
  }
  xhr.send();
  // e.preventDefault();
}
//////////////////////////////////////////////////////
// END updateProccess_print(e) UPDATE
//////////////////////////////////////////////////////

//////////////////////////////////////////////////////
// START updateBottleBeers(e) UPDATE
//////////////////////////////////////////////////////
function updateBottleBeers(e) {
  // console.log('*************TESTING updateBottleBeers*************');
  const xhr = new XMLHttpRequest();
  // Open
  xhr.open('POST', '/_bottle_beers', true);
  xhr.onload = function() {
    if (this.status === 200) {
      // console.log(this.responseText);
      let data = JSON.parse(this.responseText);
      ///////////////////////////////////////////////
      // START bottle_beers.html UPDATE
      ///////////////////////////////////////////////
      let beerListDivBB = document.getElementsByClassName('beer-list-div-bb');
      let htmlStuffBB = '';
      htmlStuffBB += `<ul id="bottle-beers-list" class='beer-list-loop-pp list-group-flush'>`;
      data.forEach(function(beer){
        let draftBottleSelection = beer.draft_bottle_selection;
        let dbs = draftBottleSelection.split(' ');
        let inBottleList = false;
        dbs = dbs.map(function(item){
          if (item === 'Bottle' || item === 'Can') {
            inBottleList = true;
          }
        });
        if (inBottleList) {

          htmlStuffBB += `<li id="" class='list-group-item-bb list-group-item'>${beer.id}.
          <span class="larger-text txt-clr-grn">${beer.name}</span>
          - <span>${draftBottleSelection}</span>
          - <span class="bold-font italic-font">${beer.style}</span>
          - ${beer.abv}% ABV - ${beer.ibu} IBU - ${beer.location}
          <span>${draftBottleSelection}</span>
          - <span class="italic-font">${beer.brewery}</span></li>`;
        }
      });
      htmlStuffBB += `</ul>`;
      if (beerListDivBB[0] !== undefined) {
        beerListDivBB[0].innerHTML = htmlStuffBB;
      }
      ///////////////////////////////////////////////
      // END bottle_beers.html UPDATE
      ///////////////////////////////////////////////
    }
  }
  xhr.send();
  // e.preventDefault();
}
//////////////////////////////////////////////////////
// END updateBottleBeers(e) UPDATE
//////////////////////////////////////////////////////

//////////////////////////////////////////////////////
// START EASY AJAX.JS updateOnTapCurrent()
//////////////////////////////////////////////////////
function updateOnTapCurrent() {
  const http = new easyHTTP;
  // Create POST
  http.postRecieve('/update', function(err, post) {
    // console.log('****************updateTappingNext*****************')
    if (err) {
      console.log(err);
    } else {
      tappingCurrent(post);
    }
  });
}
function tappingCurrent(data) {
  data = JSON.parse(data);
  data = data.slice(0,16);
  let tapCurrentTr = document.querySelectorAll(".currentBeer");
  let x = 0;
  let trInnerHTML = "";
  if (tapCurrentTr !== null) {
    data.forEach(function(beer){
      trInnerHTML = `${beer.brewery} ${beer.name}`;
      if (tapCurrentTr[x] != undefined) {
        tapCurrentTr[x].innerHTML = trInnerHTML;
      }
      x++;
    });
  }
}
//////////////////////////////////////////////////////
// END EASY AJAX.JS updateOnTapCurrent()
//////////////////////////////////////////////////////
//////////////////////////////////////////////////////
// START EASY AJAX.JS updateOnTapNext()
//////////////////////////////////////////////////////
function updateOnTapNext() {
  const http = new easyHTTP;
  // Create POST
  http.postRecieve('/updateTappingNext', function(err, post) {
    // console.log('****************updateTappingNext*****************')
    if (err) {
      console.log(err);
    } else {
      tappingNext(post);
    }
  });
}
function tappingNext(data) {
  data = JSON.parse(data);
  let tapNextTr = document.querySelectorAll(".nextBeer");
  let x = 0;
  let trInnerHTML = "";
  data.forEach(function(beer){
    trInnerHTML = `${beer.brewery} ${beer.name}`;
    if (tapNextTr[x] != undefined) {
      tapNextTr[x].innerHTML = trInnerHTML;
    }
    x++;
  });
}
//////////////////////////////////////////////////////
// END EASY AJAX.JS updateOnTapNext()
//////////////////////////////////////////////////////

//////////////////////////////////////////////////////
// START AJAX updateExample6()
//////////////////////////////////////////////////////
function updateExample6() {
    const http = new easyHTTP;
    // Create POST
    http.postRecieve('/_screen_display', function(err, post) {
      // console.log('************NEW POST BEGIN postRecieve***************');
      console.log(JSON.parse(post).userSettings);
      if (err) {
        console.log(err);
      } else {
        let data = post;
        let beers = JSON.parse(data).beers;
        let events = JSON.parse(data).events;
        let templates = JSON.parse(data).userSettings.templates;
        let settings = JSON.parse(data).userSettings;
        // console.log(settings);

        if (templates == '2 Columns, Names') {
          // console.log("2 Columns, Names");
          screenTemplate.updateDisplayScreen(beers, events, settings);
          // console.log(beers);
        } else if (templates == '2 Columns, Artist Time') {
          screenTemplate.updateDisplayScreenArtistTime(beers, events, settings);
        } else if (templates == '2 Columns, Names, ABV') {
          // console.log('2 Columns, Names, ABV');
          screenTemplate.twoColNameAbv(beers, settings);
          // console.log(beers);
        } else if (templates == '2 Columns, Names, ABV, IBU'){
          // console.log('2 Columns, Names, ABV, IBU');
          screenTemplate.exampleSix(beers, settings);
          // console.log(beers);
        } else {
          screenTemplate.exampleSix(beers, settings);
          // console.log(beers);
        }
      }
    }); // END function http.postRecieve()
//////////////////////////////////////////////////////
// END AJAX updateExample6()
//////////////////////////////////////////////////////

  // console.log('UPDATE EXAMPLE 6')
//???????????????????????????????????????????????????
// BEGIN ASYNC AWAIT
//???????????????????????????????????????????????????
  // screen.screenUpdate()
  // .then(data => {
  //   // console.log(data.result);
  //   // console.log(data.result.userSettings.templates);
  //   if (data.result.userSettings.templates == '2 Columns, Names') {
  //     console.log("2 Columns, Names");
  //     beers = data.result.beers;
  //     events = data.result.events;
  //     // console.log(beers);
  //     // console.log(events);
  //     updateDisplayScreen(beers, events);
  //     console.log(beers);
  //   } else if (data.result.userSettings.templates == '2 Columns, Names, ABV') {
  //     console.log('2 Columns, Names, ABV');
  //     twoColNameAbv(beers);
  //     console.log(beers);
  //   } else if (data.result.userSettings.templates == '2 Columns, Names, ABV, IBU'){
  //     console.log('2 Columns, Names, ABV, IBU');
  //     exampleSix(beers);
  //     console.log(beers);
  //   } else {
  //     exampleSix(beers);
  //     console.log(beers);
  //   }
  // });
//???????????????????????????????????????????????????
// END ASYNC AWAIT
//???????????????????????????????????????????????????
} // END FUNCTION updateExample6()




//////////////////////////////////////////////////////
// START loadTicker()
//////////////////////////////////////////////////////
function loadTicker() {
  // console.log('*************TESTING loadTicker*************');
  const xhr = new XMLHttpRequest();

  xhr.open('POST', '/update', true);
  xhr.onload = function() {

    if (this.status === 200) {
      let data = JSON.parse(this.responseText);
      let data1722 = data.slice(16,22);
      let tickerhtml = '';

      let beer1 = document.querySelector(".info1");
      tickerhtml = `${data1722[0].name}`;
      if (beer1 != null) {
        beer1.innerHTML = tickerhtml;
        let width = beer1.offsetWidth;
        // console.log("info1 width: " + width);
      }
      let beer2 = document.querySelector(".info2");
      tickerhtml = `${data1722[1].name}`;
      if (beer2 != null) {
        beer2.innerHTML = tickerhtml;
        let width = beer2.offsetWidth;
        // console.log("info2 width: " + width);
      }
      let beer3 = document.querySelector(".info3");
      tickerhtml = `${data1722[2].name}`;
      if (beer3 != null) {
        beer3.innerHTML = tickerhtml;
        let width = beer3.offsetWidth;
        // console.log("info3 width: " + width);
      }
      let beer4 = document.querySelector(".info4");
      tickerhtml = `${data1722[3].name}`;
      if (beer4 != null) {
        beer4.innerHTML = tickerhtml;
        let width = beer4.offsetWidth;
        // console.log("info4 width: " + width);
      }
      let beer5 = document.querySelector(".info5");
      tickerhtml = `${data1722[4].name}`;
      if (beer5 != null) {
        beer5.innerHTML = tickerhtml;
        let width = beer5.offsetWidth;
        // console.log("info5 width: " + width);
      }
      let beer6 = document.querySelector(".info6");
      tickerhtml = `${data1722[5].description}`;
      if (beer6 != null) {
        beer6.innerHTML = tickerhtml;
        let width = beer6.offsetWidth;
        // console.log("info6 width: " + width);
      }
    }
  }
  xhr.send();
  // e.preventDefault();
}
//////////////////////////////////////////////////////
// END loadTicker()
//////////////////////////////////////////////////////
