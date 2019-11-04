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
  let elInnerWidth = el.offsetWidth;
  let elWidthStyle = getComputedStyle(el);
  let elMarginLeftWidth = parseInt(elWidthStyle.marginLeft);
  let elMarginRightWidth = parseInt(elWidthStyle.marginRight);
  elTotalWidth = 0;
  elTotalWidth += elInnerWidth;
  elTotalWidth += elMarginLeftWidth;
  elTotalWidth += elMarginRightWidth;
  return elTotalWidth;
}

function getMovement(liTicker) {
    let liTotalWidth = 0;
    let tickerWidth = 0;
    let totalDivTicker = 0;
    let totalLiWidth = 0;
    liTicker.forEach(function(tick){
      let elWidth = getElementWidth(tick);
      let beforePseudoWidth = getPseudoElementWidth(tick, "before", "width");
      let afterPseudoWidth = getPseudoElementWidth(tick, "after", "width");
      totalLiWidth += beforePseudoWidth + afterPseudoWidth + elWidth;
    });
    widthMovement = "translateX(-" + totalLiWidth + "px)";
  return widthMovement;
}

function getDuration(liTicker) {
      let liTotalWidth = 0;
      let tickerWidth = 0;
      let totalDivTicker = 0;
      let totalLiWidth = 0;
      liTicker.forEach(function(tick){
        let elWidth = getElementWidth(tick);
        let beforePseudoWidth = getPseudoElementWidth(tick, "before", "width");
        let afterPseudoWidth = getPseudoElementWidth(tick, "after", "width");
        totalLiWidth += beforePseudoWidth + afterPseudoWidth + elWidth;
      });

  widthMovement = "translateX(-" + totalLiWidth + "px)";
  let tickerDuration = totalLiWidth * 10;
  return tickerDuration;
}
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
