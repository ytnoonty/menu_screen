function getPseudoElementWidth(el, position, property) {
  let totalElWidth = 0;
  position = ":" + position;
  var elWidth = window.getComputedStyle(
    el, position
  ).getPropertyValue(property);

  elWidth = parseInt(elWidth.slice(0,2));
  if (isNaN(elWidth)) {
    elWidth = 0;
  } else {
  }

  totalElWidth = elWidth;
  // console.log("position: " + position + " " + totalElWidth);
  return totalElWidth;
}

function getElementWidth(el) {
  // console.log("FINDING THE ELEMENT WIDTH");
  // console.log(el);
  let elInnerWidth = el.offsetWidth;
  let elWidthStyle = getComputedStyle(el);
  let elMarginLeftWidth = parseInt(elWidthStyle.marginLeft);
  let elMarginRightWidth = parseInt(elWidthStyle.marginRight);
  elTotalWidth = 0;
  elTotalWidth += elInnerWidth;
  elTotalWidth += elMarginLeftWidth;
  elTotalWidth += elMarginRightWidth;
  // console.log("elInnerTotalWidth = " + elTotalWidth);
  // console.log(" ");
  return elTotalWidth;
}


// function getPseudoElementWidth(el) {
//   let infoWidthBefore = window.getComputedStyle(
//     el, ":before"
//   ).getPropertyValue("width");
//   let infoWidthAfter = window.getComputedStyle(
//     el, ":after"
//   ).getPropertyValue("width");
//   infoWidthBefore = parseInt(infoWidthBefore.slice(0,2));
//   infoWidthAfter = parseInt(infoWidthAfter.slice(0,2));
//   if (isNaN(infoWidthBefore)) {
//     infoWidthBefore = 0;
//   } else {
//   }
//   if (isNaN(infoWidthAfter)) {
//     infoWidthAfter = 0;
//   } else {
//   }
//   totalInfoWidth = infoWidthBefore + infoWidthAfter;
//   console.log(totalInfoWidth);
// }

// function moveTheStuff() {
//   console.log("************MOVING STUFF ALL OVER**************");
//   // let divTicker = document.querySelector(".ticker");
//   // let liTicker = document.querySelectorAll(".info");
//   // let ulTicker = document.querySelector(".list-bts-coming-soon");
//   let liTotalWidth = 0;
//   let tickerWidth = 0;
//   let totalDivTicker = 0;
//   let totalLiWidth = 0;
//   liTicker.forEach(function(tick){
//     let liInnerWidth = tick.offsetWidth;
//     let widthStyle = getComputedStyle(tick);
//     let marginLeftWidth = parseInt(widthStyle.marginLeft);
//     let marginRightWidth = parseInt(widthStyle.marginRight);
//
//     let beforePseudoWidth = getPseudoElementWidth(tick, "before", "width");
//     let afterPseudoWidth = getPseudoElementWidth(tick, "after", "width");
//     let elWidth = getElementWidth(tick);
//     let widthMovement = "";
//     // console.log("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!");
//     // console.log("Total element width: " + (beforePseudoWidth + afterPseudoWidth + elWidth));
//     totalLiWidth += beforePseudoWidth + afterPseudoWidth + elWidth;
//     // console.log("totalLiWidth: " + totalLiWidth);
//     // console.log("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!");
//     liTotalWidth = 0;
//     // liTotalWidth += totalInfoWidth;
//     liTotalWidth += liInnerWidth;
//     liTotalWidth += marginLeftWidth;
//     liTotalWidth += marginRightWidth;
//     // console.log("liTotalWidth = " + liTotalWidth);
//     tickerWidth += liTotalWidth;
//     // console.log("tickerWidth = " + tickerWidth);
//     // console.log(" ");
//   });
//   widthMovement = "translateX(-" + totalLiWidth + "px)";
//   // console.log("widthMovement = " + widthMovement);
//   let tickerDuration = totalLiWidth * 10;
//   // console.log("tickerDuration = " + tickerDuration);
//   animateTicker(divTicker, widthMovement, tickerDuration);
//
// }

// let divTicker = document.querySelector(".ticker");
// let infoTicker = document.querySelectorAll(".info");
// let ulTicker = document.querySelector(".list-bts-coming-soon");

// console.log(liTicker);
function getMovement(liTicker) {
  // console.log("************getMovement()**************");
    // let divTicker = document.querySelector(".ticker");
    // console.log(divTicker);
    // let liTicker = document.querySelectorAll(".info");
    // console.log(liTicker);
    // let ulTicker = document.querySelector(".list-bts-coming-soon");
    // console.log(ulTicker);
    let liTotalWidth = 0;
    let tickerWidth = 0;
    let totalDivTicker = 0;
    let totalLiWidth = 0;
    liTicker.forEach(function(tick){
      // console.log(tick);
      // let liInnerWidth = tick.offsetWidth;
      // let widthStyle = getComputedStyle(tick);
      // let marginLeftWidth = parseInt(widthStyle.marginLeft);
      // let marginRightWidth = parseInt(widthStyle.marginRight);
      // liTotalWidth += liInnerWidth;
      // liTotalWidth += marginLeftWidth;
      // liTotalWidth += marginRightWidth;
      // console.log("liTotalWidth = " + liTotalWidth);

      let elWidth = getElementWidth(tick);
      let beforePseudoWidth = getPseudoElementWidth(tick, "before", "width");
      let afterPseudoWidth = getPseudoElementWidth(tick, "after", "width");
      totalLiWidth += beforePseudoWidth + afterPseudoWidth + elWidth;
      //
      //
      // let widthMovement = "";
      // // console.log("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!");
      // console.log("Total element width: " + (beforePseudoWidth + afterPseudoWidth + elWidth));
      // console.log("totalLiWidth: " + totalLiWidth);
      // console.log("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!");
      // liTotalWidth = 0;
      // // liTotalWidth += totalInfoWidth;
      //
      // tickerWidth += liTotalWidth;
      // console.log("tickerWidth = " + tickerWidth);
      // console.log(" ");
    });
    widthMovement = "translateX(-" + totalLiWidth + "px)";
    // console.log("widthMovement = " + widthMovement);
  return widthMovement;
}

function getDuration(liTicker) {
  // console.log("************getDuration()**************");
      // let divTicker = document.querySelector(".ticker");
      // console.log(divTicker);
      // let liTicker = document.querySelectorAll(".info");
      // console.log(liTicker);
      // let ulTicker = document.querySelector(".list-bts-coming-soon");
      // console.log(ulTicker);
      let liTotalWidth = 0;
      let tickerWidth = 0;
      let totalDivTicker = 0;
      let totalLiWidth = 0;
      liTicker.forEach(function(tick){
        // console.log(tick);
        // let liInnerWidth = tick.offsetWidth;
        // let widthStyle = getComputedStyle(tick);
        // let marginLeftWidth = parseInt(widthStyle.marginLeft);
        // let marginRightWidth = parseInt(widthStyle.marginRight);
        // liTotalWidth += liInnerWidth;
        // liTotalWidth += marginLeftWidth;
        // liTotalWidth += marginRightWidth;
        // console.log("liTotalWidth = " + liTotalWidth);

        let elWidth = getElementWidth(tick);
        let beforePseudoWidth = getPseudoElementWidth(tick, "before", "width");
        let afterPseudoWidth = getPseudoElementWidth(tick, "after", "width");
        totalLiWidth += beforePseudoWidth + afterPseudoWidth + elWidth;
        //
        //
        // let widthMovement = "";
        // // console.log("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!");
        // console.log("Total element width: " + (beforePseudoWidth + afterPseudoWidth + elWidth));
        // console.log("totalLiWidth: " + totalLiWidth);
        // console.log("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!");
        // liTotalWidth = 0;
        // // liTotalWidth += totalInfoWidth;
        //
        // tickerWidth += liTotalWidth;
        // console.log("tickerWidth = " + tickerWidth);
        // console.log(" ");
      });

  widthMovement = "translateX(-" + totalLiWidth + "px)";
  // console.log("widthMovement = " + widthMovement);
  let tickerDuration = totalLiWidth * 10;
  // console.log("tickerDuration = " + tickerDuration);
  return tickerDuration;
}

// let divTicker = document.querySelector(".ticker");
// let movement = getMovement(infoTicker);
// let duration = getDuration(infoTicker);
// if (divTicker) {
//   animateTicker(divTicker, movement, duration);
// }
function animateTicker(el, movement, duration) {
  el.animate([
    { transform: 'translateX(100vw)'},
    { transform: movement}
  ], {
    duration: duration,
    iterations: Infinity
  });
}





// Init Beer
const beer = new Beer();
// Search input for beer on the dashboard
const searchBeerDashboard = document.getElementById('dashboard-search-beer');
const dashboardBeerInfo = document.getElementById('dashboard-beer-info');
const dashboardClearSearchBtn = document.getElementById('clear-dash-search');
const dashboardTable = document.querySelectorAll('table tr');
const dashboardTableRowName = document.querySelectorAll('.row-name');

document.addEventListener('click', (e)=>{
  if (e.target.classList.contains('toggle-table')){
    console.log('TOGGLE-TABLE');
    e.target.parentElement.nextElementSibling.firstElementChild.classList.toggle('d-none');
  }
  // e.preventDefault();
});

if (searchBeerDashboard !== null) {
  // Search input event listener
  searchBeerDashboard.addEventListener('keyup', (e) => {
    // Get input text
    const userText = e.target.value.toLowerCase();
    if (userText !== ''){
      // console.log(userText);
      // console.log(dashboardTable);
      dashboardTableRowName.forEach(tableRow => {
        let name = tableRow.innerText.split('\t')[0];
        // console.log(name);
        if (name.toLowerCase().indexOf(userText) > -1) {
          // console.log(name);
          // console.log(tableRow);
          tableRow.classList.remove('d-none');
        } else {
          tableRow.classList.add('d-none');
        }
      });
      // dashboardTable.forEach(table => {
      //   console.log(table.firstElementChild);
      // });


      // Clear dashboard beers
      // uiClearBeerInfo();
      // // Make http call to get searched beer
      // beer.getBeer(userText)
      //   .then(data => {
      //     if (data.result === null){
      //       // Show alert if not found
      //       console.log('results === null');
      //     } else {
      //       // Show beer info
      //       uiPopulateBeersInfo(data.result);
      //     }
      //   })
      //   .catch(err => {
      //     console.log(err);
      //   })
    } else {
      dashboardTableRowName.forEach(tableRow => {
        tableRow.classList.remove('d-none');
      });
      // Clear dashboard beers
      // uiClearBeerInfo();
      // Make http call to get all beers
      // console.log('CLEARING UI NOW');
      // beer.getBeerList()
      //   .then(data => {
      //     console.log('DATA IS GOOD');
      //     // Populate dashboard
      //     uiPopulateBeersInfo(data.results);
      //   })
      //   .catch(err => {
      //     console.log(err);
      //   })

    }
  });
}

if (dashboardClearSearchBtn !== null) {
  dashboardClearSearchBtn.addEventListener('click', (e) => {
    // Clear dashboard search input
    if (searchBeerDashboard.value !== ''){
        // Clear dashboard beers
        uiClearBeerInfo();
        // Make http call to get all beers
        console.log('CLEARING UI NOW');
        beer.getBeerList()
          .then(data => {
            console.log('DATA IS GOOD');
            // Populate dashboard
            uiPopulateBeersInfo(data.results);
          })
          .catch(err => {
            console.log(err);
          })
    }
    searchBeerDashboard.value = '';
    searchBeerDashboard.focus();
  });
}

function uiPopulateBeersInfo(beers) {
  let dashboardTable = document.createElement('table');
  dashboardTable.className = 'mt-3 table table-striped';
  beers.forEach(beer => {
    console.log(beer);
    dashboardTable.innerHTML += `
      <tr>
        <th class="toggle-table">${beer.name}</th>
        <td><a href="edit_beer/${beer.id}" class="btn btn-default pull-right">Edit</a></td>
        <td>
          <form action="/delete_beer/${beer.id}" method="post">
            <input type="hidden" name="_method" value="DELETE">
            <input type="submit" value="Delete" class="btn btn-danger">
          </form>
        </td>
      </tr>
      <tr>
        <td colspan="2" class="d-none animate-table">
          <div class="row">
            <div class="col-5">ID:</div>
            <div class="col-7">${beer.id}</div>
          </div>
          <div class="row">
            <div class="col-5">Style:</div>
            <div class="col-7">${beer.style}</div>
          </div>
          <div class="row">
            <div class="col-5">ABV:</div>
            <div class="col-7">${beer.abv}</div>
          </div>
          <div class="row">
            <div class="col-5">IBU:</div>
            <div class="col-7">${beer.ibu}</div>
          </div>
          <div class="row">
            <div class="col-5">Brewery:</div>
            <div class="col-7">${beer.brewery}</div>
          </div>
          <div class="row">
            <div class="col-5">Location:</div>
            <div class="col-7">${beer.location}</div>
          </div>
          <div class="row">
            <div class="col-5">Website:</div>
            <div class="col-7">${beer.website}</div>
          </div>
          <div class="row">
            <div class="col-5">Description:</div>
            <div class="col-7">${beer.description}</div>
          </div>
          <div class="row">
            <div class="col-5">Draft / Bottle:</div>
            <div class="col-7">${beer.draft_bottle_selection}</div>
          </div>
        </td>
      </tr>
    `;
  });
  dashboardBeerInfo.appendChild(dashboardTable);
}

function uiClearBeerInfo() {
  dashboardBeerInfo.innerHTML = '';
}

function uiShowBeerInfo(beer){
  beer = beer.result;
  console.log(beer);
  dashboardBeerInfo.innerHTML = `
    <table class="mt-3 table table-striped">
      <tr>
        <th class="toggle-table">${beer.name}</th>
        <td><a href="edit_beer/${beer.id}" class="btn btn-default pull-right">Edit</a></td>
        <td>
          <form action="/delete_beer/${beer.id}" method="post">
            <input type="hidden" name="_method" value="DELETE">
            <input type="submit" value="Delete" class="btn btn-danger">
          </form>
        </td>
      </tr>
      <tr>
        <td colspan="2" class="d-none animate-table">
          <div class="row">
            <div class="col-5">ID:</div>
            <div class="col-7">${beer.id}</div>
          </div>
          <div class="row">
            <div class="col-5">Style:</div>
            <div class="col-7">${beer.style}</div>
          </div>
          <div class="row">
            <div class="col-5">ABV:</div>
            <div class="col-7">${beer.abv}</div>
          </div>
          <div class="row">
            <div class="col-5">IBU:</div>
            <div class="col-7">${beer.ibu}</div>
          </div>
          <div class="row">
            <div class="col-5">Brewery:</div>
            <div class="col-7">${beer.brewery}</div>
          </div>
          <div class="row">
            <div class="col-5">Location:</div>
            <div class="col-7">${beer.location}</div>
          </div>
          <div class="row">
            <div class="col-5">Website:</div>
            <div class="col-7">${beer.website}</div>
          </div>
          <div class="row">
            <div class="col-5">Description:</div>
            <div class="col-7">${beer.description}</div>
          </div>
          <div class="row">
            <div class="col-5">Draft / Bottle:</div>
            <div class="col-7">${beer.draft_bottle_selection}</div>
          </div>
        </td>
      </tr>
    </table>`;
}
