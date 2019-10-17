// Init Untappd
const untappd = new Untappd;
// Init Wine
const wine = new Wine;
// Init UI
const ui = new UI;
// using ajax
const http = new easyHTTP();


// Search input
const searchBeer = document.getElementById('searchBeer');
const searchBeerBtn = document.getElementById('search-beer-btn');
const winelistMenu = document.getElementById('winelist-menu');
const winelistDescription = document.getElementById('winelist-description');
let searchListHistory = "";

// wine list table heading
const updateWinelist = document.querySelector('.update-wine-list');

if (searchBeer !== null) {
  // hit enter key to search for info
  searchBeer.addEventListener('keyup', (e) => {
    // Get input text
    const userText = e.target.value;
    // keycode 13 is enter key
    if (e.keyCode === 13) {
      if(userText !== '') {
        untappd.getBeerByName(userText)
        .then(data => {
          if (data.results.message === 'Not Found') {
            // Show alert

          } else {
            // Show results
            searchListHistory = data.results;
            ui.showBeerList(data.results);
          }
        });
      } else {
        // Clear results
        // ui.clearResults();
        // console.log('Put something in me!!!!!!!!!!!');
      }
    }
  });

  // click button to search for info
  searchBeerBtn.addEventListener('click', (e) => {
    // Get input text
    const userText = searchBeer.value;
    if(userText !== '') {
      untappd.getBeerByName(userText)
      .then(data => {
        if (data.results.message === 'Not Found') {
          // Show alert

        } else {
          // Show results
          searchListHistory = data.results;
          ui.showBeerList(data.results);
        }
      });
    } else {
      // Clear results
      // ui.clearResults();
      // console.log('Put something in me!!!!!!!!!!!');
    }
  });


  document.addEventListener('click', (e) => {
    let elClass = e.target.parentElement.className;
    if (elClass === 'beer-tr') {
      let beerId = e.target.parentElement.firstElementChild.innerHTML;
      untappd.getBeerById(beerId)
      .then(data => {
        // console.log(data);
        ui.showBeerCandidate(data.singleResult);
      });
    }
    if (e.target.classList.contains('add-beer-to-db')) {
      let beerData = {
        "id": "",
        "name": "",
        "style": "",
        "abv":"",
        "ibu":"",
        "brewery":"",
        "location":"",
        "website":"",
        "description":"",
        "draftbottleselection":""
      }
      let beerInfo = e.target.parentElement.parentElement;
      untappd.beer.id = beerInfo.firstElementChild.innerText;
      untappd.beer.name = beerInfo.firstElementChild.nextElementSibling.innerText;
      untappd.beer.style = beerInfo.firstElementChild.nextElementSibling.nextElementSibling.innerText;
      untappd.beer.abv = beerInfo.firstElementChild.nextElementSibling.nextElementSibling.nextElementSibling.innerText;
      untappd.beer.ibu = beerInfo.firstElementChild.nextElementSibling.nextElementSibling.nextElementSibling.nextElementSibling.innerText;
      untappd.beer.brewery = beerInfo.firstElementChild.nextElementSibling.nextElementSibling.nextElementSibling.nextElementSibling.nextElementSibling.innerText;
      untappd.beer.location = beerInfo.firstElementChild.nextElementSibling.nextElementSibling.nextElementSibling.nextElementSibling.nextElementSibling.nextElementSibling.innerText;
      untappd.beer.website = beerInfo.firstElementChild.nextElementSibling.nextElementSibling.nextElementSibling.nextElementSibling.nextElementSibling.nextElementSibling.nextElementSibling.innerText;
      untappd.beer.description = beerInfo.firstElementChild.nextElementSibling.nextElementSibling.nextElementSibling.nextElementSibling.nextElementSibling.nextElementSibling.nextElementSibling.nextElementSibling.innerText;
      untappd.beer.draftbottleselection = document.querySelector('input[type="radio"][name=beer][checked=true]').value;
      beerData.id = untappd.beer.id;
      beerData.name = untappd.beer.name;
      beerData.style = untappd.beer.style;
      beerData.abv = untappd.beer.abv;
      beerData.ibu = untappd.beer.ibu;
      beerData.brewery = untappd.beer.brewery;
      beerData.location = untappd.beer.location;
      beerData.website = untappd.beer.website;
      beerData.description = untappd.beer.description;
      beerData.draftbottleselection = untappd.beer.draftbottleselection;
      // console.log(untappd.beer.id +
      //   untappd.beer.name +
      //   untappd.beer.style +
      //   untappd.beer.abv +
      //   untappd.beer.ibu +
      //   untappd.beer.brewery +
      //   untappd.beer.location +
      //   untappd.beer.website +
      //   untappd.beer.description +
      //   untappd.beer.draftbottleselection
      // );
      // console.log(untappd.beer);
      // console.log(beerData);
      const http = new easyHTTP();
      // Create POST
      http.postSendRecieve('/addUntappd', beerData, function(err, post){
        if (err) {
          console.log(err);
        } else {

          // console.log("sent data and recieving data");
          // console.log(post);
          ui.showAddedBeer(post);
        }
      });
    }
    if (e.target.classList.contains('btn-cancel')) {
      let checked = document.querySelector('input[type="radio"][name=beer][checked=true]');
      // console.log(checked.value);
      // console.log(searchListHistory);
      ui.showBeerList(searchListHistory);
    }
    if (e.target.classList.contains('bottle-draft')) {
      e.target.parentElement.parentElement.firstElementChild.firstElementChild.setAttribute("checked", false);
      e.target.parentElement.parentElement.firstElementChild.nextElementSibling.firstElementChild.setAttribute("checked", false);
      e.target.parentElement.parentElement.firstElementChild.nextElementSibling.nextElementSibling.firstElementChild.setAttribute("checked", false);
      e.target.setAttribute("checked", true);
      // console.log(e.target.parentElement.parentElement.firstElementChild.firstElementChild);
      // console.log(e.target.parentElement.parentElement.firstElementChild.nextElementSibling.firstElementChild);
      // console.log(e.target.parentElement.parentElement.firstElementChild.nextElementSibling.nextElementSibling.firstElementChild);
      // console.log("");
    }
  });
}


if (updateWinelist !== null) {
  updateWinelist.addEventListener('click', (e) => {
    loadNewDashWinelist();
  });
}
function loadNewDashWinelist() {
  // wine-list
  const dashWineList = document.getElementById('dash-wine-list');
  dashWineList.innerHTML = 'dashWineList';
  // console.log('UPDATE WINELIST');
  http.postRecieve('/_getwines', function(err, post){
    if (err) {
      console.log(err);
    } else {
      // console.log("recieving data");
      // console.log(post);
      ui.showDashWineList(post);
    }
  });

  setTimeout(loadNewDashWinelist, 1000);
}


if (winelistMenu != null){
  winelistMenu.addEventListener('click', (e)=> {
    updateCurrentWinelist();
  });
}

updateCurrentWinelist();
function updateCurrentWinelist(){
  wine.getCurrentWinelist()
  .then(data => {
    ui.updateWinelist(data.results);
  });

  setTimeout(updateCurrentWinelist, 1000);
}

if (winelistDescription != null){
  winelistDescription.addEventListener('click', (e)=> {
    updateCurrentWinelistDescription();
  });
}

updateCurrentWinelistDescription();
function updateCurrentWinelistDescription(){
  wine.getCurrentWinelist()
  .then(data => {
    ui.updateWinelistDescription(data.results);
  });

  setTimeout(updateCurrentWinelistDescription, 1000);
}
