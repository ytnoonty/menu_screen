// (function(){
//   // Declare private vars and funcitons
//   return {
//     // Declare public vars and funcitons
//   }
// })();
////////////////////////////////////////////////////////////////////////////////
// Storage Controller
////////////////////////////////////////////////////////////////////////////////

////////////////////////////////////////////////////////////////////////////////
// User Controller
////////////////////////////////////////////////////////////////////////////////
const UserCtrl = (function() {
  const User = function(){

  }

  async function fetchUserData(userData) {
    // console.log("FETCHING USER DATA");
    // console.log(userData);
    const res = await fetch('/_logged_in_user_data', {
      method: "POST",
      credentials: "include",
      body: JSON.stringify(userData),
      cache: "no-cache",
      headers: new Headers({
        "content-type": "application/json"
      })
    });
    const data = await res.json();
    // console.log(data);
    return data;
  }

  // get username from url to use if user not logged in and need to use the
  // screen for a tablet, beers_display_screen, or a website
  const getUserNameFromURL = () => {
    // console.log('**************************************************');
    // console.log('******************GET USERNAME********************');
    // console.log('**************************************************');
    let currentURL = window.location.href;
    let currentSplitURL = currentURL.split('/');
    // console.log(currentSplitURL);
    let userName = currentSplitURL[4];
    let screenNumber = currentSplitURL[5];

    // console.log(userName, screenNumber);
    return { "userName": userName, "screenNumber": screenNumber }
  }

  return {
    callFetchUserData: function(data) {
      return fetchUserData(data);
    },
    callGetUserNameFromURL: () => {
      return getUserNameFromURL();
    }
  }
})();

const UpdateCtrl = (function() {
  async function fetchAddUpdateScreenUI() {
    console.log("FETCHING SCREEN ADD UPDATE STATUS");
    const fetchResponse = await fetch('/_add_update_ui');
    const data = await fetchResponse.json();
    // console.log(data);
    return data;
  }

  async function fetchDeleteUpdateScreenUI() {
    console.log("FETCHING SCREEN DELETE UPDATE STATUS");
    const fetchResponse = await fetch('/_delete_update_ui');
    const data = await fetchResponse.json();
    // console.log(data);
    return data;
  }

  return {
    callFetchAddUpdateScreenUI: async function() {
      let data = await fetchAddUpdateScreenUI();
      // console.log(data);
      return data;
    },
    callFetchDeleteUpdateScreenUI: async function() {
      let data = await fetchDeleteUpdateScreenUI();
      // console.log(data);
      return data;
    },
  }
})();


////////////////////////////////////////////////////////////////////////////////
// Beer Controller
////////////////////////////////////////////////////////////////////////////////
const BeerCtrl = (function(){
  // Item Constructor
  const Item = function(id, name, style, abv, ibu, brewery, location, website, description, draftBottleSelection){
      this.id = id;
      this.name = name;
      this.style = style;
      this.abv = abv;
      this.ibu = ibu;
      this.brewery = brewery;
      this.location = location;
      this.website = website;
      this.description = description;
      this.draftBottleSelection = draftBottleSelection;
  }
  // Data Structure / State
  const data = {
    items: [
      { "id": "1","name": "Name","style": "Style","abv": "0.0","ibu": "0","brewery": "Brewery","location": "Location","website": "www.website.com","description": "Short description here.","draftBottleSelection": "Draft",}
    ],
    currentItem: null,
  }

  async function fetchBeerhistoryList(userData) {
    // console.log(userData);
    const res = await fetch('/_getTotBeerlist', {
      method: "POST",
      credentials: "include",
      body: JSON.stringify(userData),
      cache: "no-cache",
      headers: new Headers({
        "content-type": "application/json"
      })
    });
    const data = await res.json();
    // console.log(data);
    return data;
  }

  const fetchCurrentBeerList = function(template) {
    const fetchScreenUpdate = function(template) {
      fetch('/_screen_display')
      .then((res) => res.json())
      .then((data) => {
        // console.log(data);
        let userId = parseInt(data[0]['userSettings'].venue_db_id);
        // console.log(userId);
        userId = "user-id-" + userId;
        // console.log(userId);
        let userIdScreenDisplay = document.querySelector('#' + userId);
        let screenDisplay = document.querySelector('#' + userId + ' #screen-display');
        template(data[0]);
      })
    }
    fetchScreenUpdate(template);
  }

  async function fetchCurBeerlist(userData) {
    console.log(userData);
    const res = await fetch('/_getCurBeerlist', {
      method: "POST",
      credentials: "include",
      body: JSON.stringify(userData),
      cache: "no-cache",
      headers: new Headers({
        "content-type": "application/json"
      })
    });
    const data = await res.json();
    // console.log(data);
    return data;
  }

  async function fetchNextBeerlist(userData) {
    // console.log(userData);
    const res = await fetch('/_getNextBeerlist', {
      method: "POST",
      credentials: "include",
      body: JSON.stringify(userData),
      cache: "no-cache",
      headers: new Headers({
        "content-type": "application/json"
      })
    });
    const data = await res.json();
    // console.log(data);
    return data;
  }


  const fetchAddBeerToDB = function(newBeer) {
    // const addBeer = function(beer) {
      // console.log(beer);
      fetch('/_add_beer_to_list', {
        method: "POST",
        credentials: "include",
        body: JSON.stringify(newBeer),
        cache: "no-cache",
        headers: new Headers({
          "content-type": "application/json"
        })
      })
      .then((res) => res.json())
      // .then((data) => console.log(data))
    // }
    // addBeer(newBeer);
  }

  async function fetchDeleteBeerFromCurrentListDb(beerData) {
    console.log(beerData);
    const fetchResponse = await fetch('/_delete_beer_from_current_list', {
      method: "POST",
      credentials: "include",
      body: JSON.stringify(beerData),
      cache: "no-cache",
      headers: new Headers({
        "content-type": "application/json"
      })
    });
    const data = await fetchResponse.json();
    console.log(data);
    return data;
  }

  async function fetchAllTotalCurrentNextLists() {
    const fetchResponse = await fetch('/_getAllTotalCurrentNextLists');
    const data = await fetchResponse.json();
    // console.log(data);
    return data;
  }

  async function fetchBottleBeerlist(userData) {
    // console.log(userData);
    const fetchResponse = await fetch('/_getBottleBeerlist', {
      method: "POST",
      credentials: "include",
      body: JSON.stringify(userData),
      cache: "no-cache",
      headers: new Headers({
        "content-type": "application/json"
      })
    });
    const data = await fetchResponse.json();
    // console.log(data);
    return data;
  }

  const fetchAddNewBeerToDB = async data => {
    // console.log(data);
    const fetchResponse = await fetch('/_addNewBeerToDB', {
      method: "POST",
      credentials: "include",
      body: JSON.stringify(data),
      cache: "no-cache",
      headers: new Headers({
        "content-type": "application/json"
      })
    });
    data = await fetchResponse.json();
    // console.log(data);
    return data;
  }

  const createNewBeerOBJ = data => {
    let beer = {
      "name": data.beer.beer_name,
      "style": data.beer.beer_style,
      "abv": data.beer.beer_abv,
      "ibu": data.beer.beer_ibu,
      "brewery": data.beer.brewery.brewery_name,
      "location": `${data.beer.brewery.location.brewery_city}, ${data.beer.brewery.location.brewery_state}`,
      "website": data.beer.brewery.contact.url,
      "description": data.beer.beer_description,
      "draftBottle": data.draftBottleSelection,
    };
    return beer;
  }

  const sendScreenSettingsInfoToDb = async data => {
    // console.log(data);
    const fetchResponse = await fetch('/_init_new_beerscreen_settings', {
      method: "POST",
      credentials: "include",
      body: JSON.stringify(data),
      cache: "no-cache",
      headers: new Headers({
        "content-type": "application/json"
      })
    });
    data = await fetchResponse.json();
    // console.log(data);
    return data;
  }

  const removeScreenSettingsInfoFromDb = async data => {
    // console.log(data);
    const fetchResponse = await fetch('/_remove_beerscreen_settings', {
      method: "POST",
      credentials: "include",
      body: JSON.stringify(data),
      cache: "no-cache",
      headers: new Headers({
        "content-type": "application/json"
      })
    });
    data = await fetchResponse.json();
    // console.log(data);
    return data;
  }

  // Public methods
  return {
    getItems: function(){
      return data.items;
    },
    logData: function(){
      return data;
    },
    callFetchBeerhistoryList: function (data) {
      return fetchBeerhistoryList(data);
    },
    callFetchCurrentBeerList: function(template) {
      fetchCurrentBeerList(template);
    },
    callFetchCurBeerlist: function(data) {
      return fetchCurBeerlist(data);
    },
    callFetchNextBeerlist: function(data) {
      return fetchNextBeerlist(data);
    },
    callFetchAddBeerToDB: function(beer_id) {
      fetchAddBeerToDB(beer_id);
    },
    callFetchDeleteBeerFromCurrentListDb: function(beerData) {
      console.log(beerData);
      return fetchDeleteBeerFromCurrentListDb(beerData);
    },
    callFetchAllTotalCurrentNextLists: function() {
      return fetchAllTotalCurrentNextLists();
    },
    callFetchBottleBeerlist: function(data) {
      return fetchBottleBeerlist(data);
    },
    callFetchAddNewBeerToDB: function(data) {
      fetchAddNewBeerToDB(data);
    },
    callCreateNewBeerObj: function(data) {
      return createNewBeerOBJ(data);
    },
    callSendScreenSettingsInfoToDb: function(data) {
      return sendScreenSettingsInfoToDb(data);
    },
    callRemoveScreenSettingsInfoFromDb: data => {
      return removeScreenSettingsInfoFromDb(data);
    },

  }

})();
////////////////////////////////////////////////////////////////////////////////
// END BEER CONTROLLER
////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////
// BEGIN Untappd CONTROLLER
////////////////////////////////////////////////////////////////////////////////
const UntappdCtrl = (function(){
  const loadData = function(data) {
    // console.log("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~");
    // console.log("loadData(): " + data);
    // console.log("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~");
    let untappd = new Untappd;
    let beerlist = [];
    let res = untappd.getBeerByName(data)
    .then(res => {
      // console.log(res.results.response.message);
      const searchlistHistory = res.results.response.beers.items;
      // console.log(searchlistHistory);
      searchlistHistory.forEach(item => {
        const { beer, brewery } = item;
        let newBeer = { "beer": beer, "brewery": brewery };
        beerlist.push(newBeer);
      });
      // console.log(beers);
      return beerlist;
    });
    return res;
  }

  const getSingleBeerById = function(data) {
    let untappd = new Untappd;
    let res = untappd.getBeerById(data)
    .then(res => {
      let newBeer = res.singleResult.response.beer;
      return newBeer;
    });
    return res;
  }

  return {
    callLoadData: function(data) {
      return loadData(data);
    },
    callGetSingleBeerById: function(data) {
      return getSingleBeerById(data);
    }
  }
})();
////////////////////////////////////////////////////////////////////////////////
// END Untappd CONTROLLER
////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////
// BEGIN TICKER CONTROLLER
////////////////////////////////////////////////////////////////////////////////
const TickerCtrl = (function(){
  const logData = function() {
    // console.log('IN THE TICKER CONTROLLER');
  }
  async function fetchTickerInfo(userData) {
    // console.log(userData);
    const res = await fetch('/getTickerInfo', {
      method: "POST",
      credentials: "include",
      body: JSON.stringify(userData),
      cache: "no-cache",
      headers: new Headers({
        "content-type": "application/json"
      })
    });
    const data = await res.json();
    // console.log(data);
    return data;
  }

  return {
    callLogData: function() {
      logData();
    },
    callFetchTickerInfo: function(data) {
      return fetchTickerInfo(data);
    },
  }
})();
////////////////////////////////////////////////////////////////////////////////
// END TICKER CONTROLLER
////////////////////////////////////////////////////////////////////////////////

////////////////////////////////////////////////////////////////////////////////
// WINE Controller
////////////////////////////////////////////////////////////////////////////////
const WineCtrl = (function(){
  const logData = function() {
    console.log('IN THE WINE CONTROLLER');
  }

  const fetchCurrentWinelist = function(template) {
    const fetchScreenUpdate = function(template) {
      fetch('/_winemenu_list_display')
      .then((res) => res.json())
      .then((data) => {
        // console.log(data);
        template(data);
      })
    }
    fetchScreenUpdate(template);
  }

  return {
    callLogData: function() {
      logData();
    },
    callFetchCurrentWinelist: function(template) {
      fetchCurrentWinelist(template);
    },
  }
})();
////////////////////////////////////////////////////////////////////////////////
// END WINE Controller
////////////////////////////////////////////////////////////////////////////////

////////////////////////////////////////////////////////////////////////////////
// EVENT Controller
////////////////////////////////////////////////////////////////////////////////
const EventCtrl = (function(){
  async function getCurrentEventlist (userData) {
    // console.log(userData);
    const res = await fetch('/_get_event_current_list', {
      method: "POST",
      credentials: "include",
      body: JSON.stringify(userData),
      cache: "no-cache",
      headers: new Headers({
        "content-type": "application/json"
      })
    });
    const data = await res.json();
    // console.log(data);
    return data;
  }

  return {
    callGetCurrentEventlist: function(data) {
      return getCurrentEventlist(data);
    },
  }
})();
////////////////////////////////////////////////////////////////////////////////
// END EVENT CONTROLLER
////////////////////////////////////////////////////////////////////////////////

////////////////////////////////////////////////////////////////////////////////
// SETTINGS Controller
////////////////////////////////////////////////////////////////////////////////
const ScreenSettingsCtrl = (function() {
  async function fetchBeerscreenSettings(userData) {
    // console.log(userData);
    const res = await fetch('/_get_beerscreen_settings', {
      method: "POST",
      credentials: "include",
      body: JSON.stringify(userData),
      cache: "no-cache",
      headers: new Headers({
        "content-type": "application/json"
      })
    });
    const data = await res.json();
    // console.log(data);
    return data;
  }

  async function fetchNumberOfBeerscreens() {
    return await fetch('/_get_number_of_beer_screens')
    .then((res) => res.json())
    .then((data) => {
      return data;
    });
  }

  return {
    callFetchBeerscreenSettings: async function(data) {
      return await fetchBeerscreenSettings(data);
    },
    callFetchNumberOfBeerScreens: async function(data) {
      return await fetchNumberOfBeerscreens();
    }
  }
})();
////////////////////////////////////////////////////////////////////////////////
// END SETTINGS Controller
////////////////////////////////////////////////////////////////////////////////

////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////


////////////////////////////////////////////////////////////////////////////////
// UI Controller
////////////////////////////////////////////////////////////////////////////////
const UICtrl = (function(){
  const UISelectors = {
    flashMsgDiv: '#flash-msg-div',
    editBeerlistForm: '#edit-beerlist-form',
    editBeerlistBtn: '#edit-beerlist',
    settingsForm: '#settings-form',
    submitSettingsBtn: '#submit-settings-btn',
    editWinelistForm: '#edit-winelist-form',
    editWinelistBtn: '#edit-winelist-btn',

    // edit wine
    editWineForm: '#edit-wine-form',
    editWineSubmitBtn: '#edit-wine-submit-btn',

    // Add btn to the beerlist
    addBeerBtn: '#add-beer-btn',
    // Delete btn from the beerlist
    delBeerBtn: '#delete-beer-btn',
    beers: '.beer',
    beerlist: '#beerlist',
    // edit beer form
    editBeerForm: '#edit-beer-form',
    editBeerSubmitBtn: '#edit-beer-submit-btn',

    addWineForm: '#add-wine-form',
    addWineSubmitBtn: '#add-wine-submit-btn',

    editOnTapNextEditorForm: '#edit-on-tap-next-editor-form',
    editOnTapNextEditorSubmitBtn: '#edit-on-tap-next-editor-submit',

    addBeerToDbForm: '#add-beer-to-db-form',
    addBeerToDbSubmitBtn: '#add-beer-to-db-btn',
    ticker: '.ticker',
    tickerItems: '.ticker-items',
    tickerItem: '.ticker-item',

    // beer_dashboard.html clear search button
    clearDashSearch: '#clear-dash-search',
    dashboardSearchBeer: '#dashboard-search-beer',
    dashboardBeerInfo: '#dashboard-beer-info',
    dashboardTableTr: 'table tr',
    dashboardTableRowName: '.row-name',

    // tablet menu buttons
    draftBeersTabletNavBtn: '#draft-beers-tablet',
    bottleBeersTabletNavBtn: '#bottle-beers-tablet',
    winelistMenuTabletNavBtn: '#winelist-menu-tablet',
    winelistDescriptionTabletNavBtn: '#winelist-description-tablet',

    // search beer to add to list
    searchBeerText: '#search-beer',
    searchBeerBtn: '#search-beer-btn',
    searchBeerResults: '#search-beer-results',
    untappdAddBeerToDB: '.untappd-add-beer-to-db',

    // edit_beer_list.html
    beerscreenDisplayId: '#beerscreen-display-id',
    // beerscreen_settings.html
    beerSettingsScreenId: '#beerSettingsScreenId',
    // beerscreen_settings.html
    addBeerTemplateBtn: '#add-beerscreen-template-btn',
    delBeerTemplateBtn: '#del-beerscreen-template-btn',
    // beers_display_screen
    screenDisplay: '#screen-display',
    beersDisplayNavPrev: '#beers-display-nav-prev',
    beersDisplayNavNext: '#beers-display-nav-next',
  }

  // flash message dissapear after 2.5 seconds
  const hideFlashMsg = function() {
    let flashMsgDiv = document.querySelector(UISelectors.flashMsgDiv);
    setTimeout(() => {
      flashMsgDiv.style.display = 'none';
    },2500);
  }

  const loadBeerlist = function() {
    // console.log('LOAD BEERLIST');
  }

  const updateDisplayScreen = function(displayData) {
    // console.log("**************************************************************************************");
    // console.log("UPDATE DISPLAY SCREEN");
    // console.log("**************************************************************************************");
    // console.log(displayData);
    const { screenSettings } = displayData;
    // console.log(screenSettings.templateName);
    const beerscreenTemplate = new BeerTemplate;
    const eventscreenTemplate = new EventTemplate;
    let templateName = screenSettings.templateName;
    if (templateName == '2 Columns, Name, Style, ABV, IBU') {
      // console.log("**************************************************************************************");
      // console.log('IN THE DEFAULT TEMPLATE');
      // console.log("**************************************************************************************");
      beerscreenTemplate.defaultTemplate(displayData);
    } else if (templateName == '2 Columns, Name, ABV, IBU') {
      // console.log("**************************************************************************************");
      // console.log('IN THE DEFAULT TEMPLATE');
      // console.log("**************************************************************************************");
      beerscreenTemplate.defaultTemplate(displayData);
    } else if (templateName == '2 Columns, Name, Style, ABV'){
      // console.log('IN THE 2sna TEMPLATE');
      beerscreenTemplate.twoColNSAITemplate(displayData);
    } else if (templateName == '2 Columns, Name, Style'){
      // console.log('IN THE 2sn TEMPLATE');
      beerscreenTemplate.twoColNSTemplate(displayData);
    } else if (templateName == '2 Event Columns') {
      eventscreenTemplate.eventTwoColTemplate(displayData);
    }
  }
  const udpateDraftBeersPrintScreen = (displayData) => {
    const { beers } = displayData;
    // console.log('IN THE udpateBeersPrintScreen');
    const beersprintTemplate = new BeerTemplate;
    beersprintTemplate.draftBeersPrintScreenTemplate(displayData);
    // beersprintTemplate.draftBeersPrintScreenTemplate(beers);
  }
  const updateDraftBeersTabletScreen = (displayData) => {
    // console.log('IN THE updateDraftBeersTabletScreen');
    const beersprintTemplate = new BeerTemplate;
    beersprintTemplate.draftBeersTabletScreenTemplate(displayData);
    // beersprintTemplate.draftBeersTabletScreenTemplate(beers);
  }
  const updateBottleBeersTabletScreen = (displayData) => {
    // console.log(displayData);
    const { beerlist } = displayData;
    // console.log('IN THE updateBottleBeersTabletScreen');
    const beersprintTemplate = new BeerTemplate;
    beersprintTemplate.bottleBeersTabletScreenTemplate(displayData);
    // beersprintTemplate.bottleBeersTabletScreenTemplate(beers);
  }
  const updateWineTabletScreen = (displayData) => {
    // console.log(displayData);
    const wineScreenTabletTemplate = new WineTemplate;
    wineScreenTabletTemplate.wineTabletTemplate(displayData);
  }
  const updateWineDescriptionsTabletScreen = (displayData) => {
    // console.log(displayData);
    const wineScreenwineDescriptionsTabletTemplateTabletTemplate = new WineTemplate;
    wineScreenwineDescriptionsTabletTemplateTabletTemplate.wineDescriptionsTabletTemplate(displayData);
  }
  const addBeerToListEditor = (data) => {
      const addBeerToListTemplate = new BeerTemplate;
      addBeerToListTemplate.addBeerToListEditorTemplate(data);
  }
  const repaintBeerlistEditor = (data) => {
      const repaintBeerlist = new BeerTemplate;
      repaintBeerlist.repaintBeerListEditorTemplate(data);
  }
  const addBeerOnTapNextDisplay = (data) => {
    const addNextBeerDisplayTemplate = new BeerTemplate;
    addNextBeerDisplayTemplate.addBeerOnTapNextDisplayTemplate(data);
  }
  const addBeerOnTapNextEditor = (data) => {
    const addNextBeerEditorTemplate = new BeerTemplate;
    addNextBeerEditorTemplate.addBeerOnTapNextEditorTemplate(data);
  }
  const deleteBeerFromListEditor = (data) => {
    const deleteBeerFromListTemplate = new BeerTemplate;
    return deleteBeerFromListTemplate.deleteBeerFromListEditorTemplate(data);
  }
  const deleteBeerFromOnTapNextDisplay = (data) => {
    const deleteBeerFromOnTapNextDisplayTemplate = new BeerTemplate;
    deleteBeerFromOnTapNextDisplayTemplate.deleteBeerFromOnTapNextDisplayTemplate(data);
  }
  const deleteBeerFromOnTapNextEditor = (data) => {
    const deleteBeerFromOnTapNextEditorTemplate = new BeerTemplate;
    deleteBeerFromOnTapNextEditorTemplate.deleteBeerFromOnTapNextEditorTemplate(data);
  }
  const repaintBeerlistDashboard = (data) => {
    const beerDashboardTemplate = new BeerTemplate;
    beerDashboardTemplate.repaintBeerDashboard(data);
  }
  const paintUntappdSearchResultsList = (data) => {
    const searchUntappdTemplate = new BeerTemplate;
    searchUntappdTemplate.paintUntappdSearchResultsList(data);
  }
  const getBeerIdFromUI = (event) => {
    // get and return id from UI
    let id = event.target.parentElement.parentElement.querySelector('.beer-id').innerHTML;
    let radioName = `beer-${id}`;
    // console.log(radioName);
    // let querySelector = `input[value=Draft]`;
    let querySelector = `input[name=${radioName}]:checked`;
    // console.log(event.target.parentElement.parentElement.parentElement.parentElement.querySelector('input[name=radioName]:checked').value);
    let selectedRadioVal = document.querySelector(querySelector).value;
    // console.log(selectedRadioVal);
    return { "id": id, "selectedRadioVal": selectedRadioVal };
  }

  const addToEditBeerlistScreenSelect = () => {
    // get current number of beer display screens/ beersettings
    let displayScreenIdElement = document.querySelector(UISelectors.beerscreenDisplayId);
    if (displayScreenIdElement === null) {
      displayScreenIdElement = document.querySelector(UISelectors.beerSettingsScreenId);
    }
    // console.log(displayScreenIdElement);
    // grab the number of ids from the select
    let displayScreenIds = displayScreenIdElement.options.length;
    // create option element to go into the select
    let optionEl = document.createElement('option');
    // increment ids to go back on the option value
    displayScreenIds++;
    optionEl.innerText = displayScreenIds;
    optionEl.value = displayScreenIds;
    // append optionEl to select
    displayScreenIdElement.appendChild(optionEl);
    displayScreenIdElement.value = displayScreenIds;
    return displayScreenIds;
  }

  const delFromEditBeerlistScreenSelect = () => {
    // get current number of beer display screens/ beersettings
    let displayScreenIdElement = document.querySelector(UISelectors.beerscreenDisplayId);
    if (displayScreenIdElement === null) {
      displayScreenIdElement = document.querySelector(UISelectors.beerSettingsScreenId);
    }
    // console.log(displayScreenIdElement);
    // grab the number of ids from the select
    let displayScreenIds = displayScreenIdElement.options.length;
    console.log(displayScreenIds);
    // check if last element in select
    if (displayScreenIds > 1) {
      // remove() last option from select on UI
      let lastElOfScreenIdElement = displayScreenIdElement.lastElementChild;
      lastElOfScreenIdElement.remove();
      displayScreenIdElement.value = displayScreenIds - 1;
    }
    return displayScreenIds;
  }

  // Public methods
  return {
    getSelectors: function () {
      return UISelectors;
    },
    callHideFlashMsg: () => {
      hideFlashMsg();
    },
    callLoadBeerlist: () => {
      loadBeerlist();
    },
    callUpdateDisplayScreen: (data) => {
      updateDisplayScreen(data);
    },
    callUdpateDraftBeersPrintScreen: (data) => {
      udpateDraftBeersPrintScreen(data);
    },
    callUpdateDraftBeersTabletScreen: (data) => {
      updateDraftBeersTabletScreen(data);
    },
    callUpdateBottleBeersTabletScreen: (data) => {
      updateBottleBeersTabletScreen(data);
    },
    callUpdateWineTabletScreen: (data) => {
      updateWineTabletScreen(data);
    },
    callUpdateWineDescriptionsTabletScreen: (data) => {
      updateWineDescriptionsTabletScreen(data);
    },
    callAddBeerToListEditor: (data) => {
      addBeerToListEditor(data);
    },
    callRepaintBeerlistEditor: (data) => {
      repaintBeerlistEditor(data);
    },
    callAddBeerOnTapNextDisplay: (data) => {
      addBeerOnTapNextDisplay(data);
    },
    callAddBeerOnTapNextEditor: (data) => {
      addBeerOnTapNextEditor(data);
    },
    callDeleteBeerFromListEditor: (data) => {
      return deleteBeerFromListEditor(data);
    },
    callDeletBeerFromOnTapNextDisplay: (data) => {
      deleteBeerFromOnTapNextDisplay(data);
    },
    callDeletBeerFromOnTapNextEditor: (data) => {
      deleteBeerFromOnTapNextEditor(data);
    },
    callRepaintBeerlistDashboard: (data) => {
      repaintBeerlistDashboard(data);
    },
    callPaintUntappdSearchResultsList: (data) => {
      paintUntappdSearchResultsList(data);
    },
    callGetBeerIdFromUI: (event) => {
      return getBeerIdFromUI(event);
    },
    callAddToEditBeerlistScreenSelect: () => {
      return addToEditBeerlistScreenSelect();
    },
    callDelFromEditBeerlistScreenSelect: () => {
      return delFromEditBeerlistScreenSelect();
    }
  }
})();
////////////////////////////////////////////////////////////////////////////////
// END UICtrl
////////////////////////////////////////////////////////////////////////////////

////////////////////////////////////////////////////////////////////////////////
// App Controller
////////////////////////////////////////////////////////////////////////////////
const App = (function(UserCtrl, UpdateCtrl, BeerCtrl, UntappdCtrl, TickerCtrl, WineCtrl, EventCtrl, ScreenSettingsCtrl, UICtrl){
  // Get UI Selectors
  const UISelectors = UICtrl.getSelectors();

  async function getScreenInfo(userNameScreenId) {
    console.log(userNameScreenId);
    // get the current beerlist for user and screenId
    // query the DB for the current beerlist
    let currentBeers = await BeerCtrl.callFetchCurBeerlist(userNameScreenId);
    // console.log(currentBeers);
    // query the DB for the next beerlist
    let nextBeers = await BeerCtrl.callFetchNextBeerlist(userNameScreenId);
    // console.log(nextBeers);
    let beerslistTotal = await BeerCtrl.callFetchBeerhistoryList(userNameScreenId);
    // console.log(beerslistTotal);
    // query the DB for the ticker news info
    let bottleBeerlist = await BeerCtrl.callFetchBottleBeerlist(userNameScreenId);
    // console.log(bottleBeerlist);
    let tickerInfo = await TickerCtrl.callFetchTickerInfo(userNameScreenId);
    // console.log(tickerInfo)
    // query the DB for the events
    let events = await EventCtrl.callGetCurrentEventlist(userNameScreenId);
    // console.log(events);
    let userData = await UserCtrl.callFetchUserData(userNameScreenId);
    // console.log(userData);
    let screenSettings = await ScreenSettingsCtrl.callFetchBeerscreenSettings(userNameScreenId);
    // console.log(screenSettings);
    if (userData.id !== undefined){
      userData = userData.id[0];
    } else {
      userData = userNameScreenId.userId;
    }
    // console.log(userData);
    let onNext;
    if (Object.getOwnPropertyNames(currentBeers).length >= 1) {
      // console.log(currentBeers);
      currentBeers.forEach(beer => {
        onNext = beer.id_on_next;
        nextBeers.push(onNext);
      });
    }
    // console.log("onNext: " + onNext + "nextBeers: " + nextBeers);
    let displayData = {};
    displayData = {
      "currentBeers": currentBeers,
      "nextBeers": nextBeers,
      "beerslistTotal": beerslistTotal,
      "bottleBeerlist": bottleBeerlist,
      "tickerInfo": tickerInfo,
      "events": events,
      "screenSettings": screenSettings,
      "userSettings": { "venue_db_id": userData }
    }
    // console.log(displayData);
    return displayData;
  }

  async function setScreenInfo(displayData) {
    // // update all screens
    // // update edit_beer_list
    UICtrl.callAddBeerToListEditor(displayData);
    // // repaint beers_tv_screen
    UICtrl.callUpdateDisplayScreen(displayData);
    // // repaint draft_beers_print
    UICtrl.callUdpateDraftBeersPrintScreen(displayData);
    // // repaint draft_beers tablet screen
    UICtrl.callUpdateDraftBeersTabletScreen(displayData);
    // repaint on_tap_next_display
    UICtrl.callAddBeerOnTapNextDisplay(displayData);
    // repaint on_tap_next_editor
    UICtrl.callAddBeerOnTapNextEditor(displayData);
    // update bottle beer list asynconously
    UICtrl.callUpdateBottleBeersTabletScreen(displayData);
  }

  async function getUserInfo(data) {
    console.log(data);
    let userNameScreenId = UserCtrl.callGetUserNameFromURL();
    console.log(userNameScreenId);
    // get the current screenId from the select to query for the current_list of beers
    if (document.querySelector(UISelectors.beerscreenDisplayId) != null) {
      let beerscreenDisplayId = document.querySelector(UISelectors.beerscreenDisplayId).value;
      console.log(beerscreenDisplayId);
      userNameScreenId.screenNumber = beerscreenDisplayId;
    }
    userNameScreenId.userId = data.venue_db_id;
    console.log(userNameScreenId);
    return userNameScreenId;
  }

  async function updateScreens(data) {
    console.log("line 947 - udpateScreens");
    console.log(data);
    if (data !== undefined) {
      // console.log(data.updated);
      if (data.updated == true) {
        let userNameScreenId = await getUserInfo(data);
        console.log(userNameScreenId);
        let displayData = await getScreenInfo(userNameScreenId);
        console.log(displayData);
        setScreenInfo(displayData);
      }
    }
  } // end udpateScreens();


  async function initScreens(data) {
    await updateScreens(data);
  }
  async function addUpdateScreens(data) {
    // console.log("///////////////////////////////////////////////////////////////////////////");
    console.log("ADD UPDATE SCREENS");
    // console.log(data.venue_db_id);
    // console.log("///////////////////////////////////////////////////////////////////////////");
    // // add new beer to current screen edit_beer_list
    await updateScreens(data);
  }

  async function deleteUpdateScreens(data) {
    // console.log("///////////////////////////////////////////////////////////////////////////");
    console.log("DELETE UPDATE SCREENS");
    // console.log("///////////////////////////////////////////////////////////////////////////");
    // console.log(data);
    // console.log(data.venue_db_id);
    // delete beer from current screen from edit_beer_list
    // function call to delete
    // query the DB for the current beerlist
    await updateScreens(data);
  }
  async function updateBottleBeerScreen (data) {
    await updateScreens(data);
  }

  const initWineScreens = (data) => {
    if (data !== undefined) {
        // console.log(data.updated);
        if (data.updated == true) {
            WineCtrl.callFetchCurrentWinelist(UICtrl.callUpdateWineTabletScreen);
            WineCtrl.callFetchCurrentWinelist(UICtrl.callUpdateWineDescriptionsTabletScreen);
        }
    }
  }
  const editWineScreens = (data) => {
    if (data !== undefined) {
        // console.log(data.updated);
        if (data.updated == true) {
          console.log("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&");
          console.log("WINE DATA CAN AND WILL BE UPDATED NOW!")
          console.log("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&");
          WineCtrl.callFetchCurrentWinelist(UICtrl.callUpdateWineTabletScreen);
          WineCtrl.callFetchCurrentWinelist(UICtrl.callUpdateWineDescriptionsTabletScreen);
        }
    }
  }

  const updateBeerScreen = (data) => {
    if (data !== undefined) {
      // console.log(data.updated);
      if (data.updated == true) {
        console.log("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&");
        console.log("DATA CAN AND WILL BE UPDATED NOW!")
        console.log("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&");
      }
    }
  }


  // load update pusher
  const loadUpdatePusher = function() {
    ///////////////////////////////////////////////////////
    // // Enable pusher logging - don't include this in production
    // Pusher.logToConsole = true;
    Pusher.logToConsole = false;
    var addPusher = new Pusher('55b76ba88af32c57990c', {
      cluster: 'us2',
      forceTLS: true
    });
    var addChannel = addPusher.subscribe('my-update-channel');
    addChannel.bind('new-addUpdate-event', function(data) {
      // console.log('*****************************************');
      // console.log('*****************************************');
      // console.log('*****************************************');
      // console.log(data.message);
      // console.log('*****************************************');
      // console.log('*****************************************');
      // console.log('*****************************************');
      addUpdateScreens(data.message);
    });
    ///////////////////////////////////////////////////////

    ///////////////////////////////////////////////////////
    // // Enable pusher logging - don't include this in production
    // Pusher.logToConsole = true;
    Pusher.logToConsole = false;
    var deletePusher = new Pusher('55b76ba88af32c57990c', {
      cluster: 'us2',
      forceTLS: true
    });
    var deleteChannel = deletePusher.subscribe('my-update-channel');
    deleteChannel.bind('new-deleteUpdate-event', function(data) {
      // console.log(data.message);
      deleteUpdateScreens(data.message);
    });
    ///////////////////////////////////////////////////////

    ///////////////////////////////////////////////////////
    // // Enable pusher logging - don't include this in production
    // Pusher.logToConsole = true;
    Pusher.logToConsole = false;
    var nextPusher = new Pusher('55b76ba88af32c57990c', {
      cluster: 'us2',
      forceTLS: true
    });
    var updateNextChannel = nextPusher.subscribe('my-update-channel');
    updateNextChannel.bind('new-nextUpdate-event', function(data) {
      // update the next lists
      // console.log(data.message);
      initScreens(data.message);
      // let resData = await BeerCtrl.callFetchAllTotalCurrentNextLists();
      // console.log(data);
    });
    ///////////////////////////////////////////////////////
  }

  // Load pusher
  const loadPusher = function() {
    ///////////////////////////////////////////////////////
    // // Enable pusher logging - don't include this in production
    // Pusher.logToConsole = true;
    Pusher.logToConsole = false;
    var pusher = new Pusher('55b76ba88af32c57990c', {
      cluster: 'us2',
      forceTLS: true
    });
    var channel = pusher.subscribe('my-event-channel');
    channel.bind('new-event', function(data) {
      // console.log(data.message);
      initScreens(data.message);
    });
    ///////////////////////////////////////////////////////
  }

  const loadWinePusher = function() {
    ///////////////////////////////////////////////////////
    // // Enable pusher logging - don't include this in production
    // Pusher.logToConsole = true;
    Pusher.logToConsole = false;
    var pusher = new Pusher('55b76ba88af32c57990c', {
      cluster: 'us2',
      forceTLS: true
    });
    var addChannel = pusher.subscribe('wine-event-channel');
    addChannel.bind('add-wine-event', function(data) {
      // console.log(data.message);
      initWineScreens(data.message);
    });

    var editChannel = pusher.subscribe('wine-event-channel');
    editChannel.bind('edit-wine-event', function(data) {
      // console.log(data.message);
      editWineScreens(data.message);
    });
    ///////////////////////////////////////////////////////
  }

  const addWinePusher = function() {
    ///////////////////////////////////////////////////////
    // // Enable pusher logging - don't include this in production
    // Pusher.logToConsole = true;
    Pusher.logToConsole = false;
    var pusher = new Pusher('55b76ba88af32c57990c', {
      cluster: 'us2',
      forceTLS: true
    });
    var channel = pusher.subscribe('wine-event-channel');
    channel.bind('add-wine-event', function(data) {
      // console.log(data.message);
        initWineScreens(data.message);
    });
    ///////////////////////////////////////////////////////
  }

  const addBeerToDbPusher = function() {
    ///////////////////////////////////////////////////////
    // // Enable pusher logging - don't include this in production
    // Pusher.logToConsole = true;
    Pusher.logToConsole = false;
    var pusher = new Pusher('55b76ba88af32c57990c', {
      cluster: 'us2',
      forceTLS: true
    });
    var addBeerChannel = pusher.subscribe('myAddBeer-event-channel');
    addBeerChannel.bind('addBeerToDb-event', function(data) {
      console.log('LINE 826');
      // console.log(data.message);
      updateBottleBeerScreen(data.message);
    });
    ///////////////////////////////////////////////////////
  }
  const editBeerToDbPusher = function() {
    ///////////////////////////////////////////////////////
    // // Enable pusher logging - don't include this in production
    // Pusher.logToConsole = true;
    Pusher.logToConsole = false;
    var pusher = new Pusher('55b76ba88af32c57990c', {
      cluster: 'us2',
      forceTLS: true
    });
    var editBeerChannel = pusher.subscribe('myEditBeer-evemt-channel');
    editBeerChannel.bind('editBeerToDb-event', function(data) {
      console.log('LINE 842');
      // console.log(data.message);
      updateBottleBeerScreen(data.message);
    });
    ///////////////////////////////////////////////////////
  }

  const delBeerFromDbPusher = function() {
    ///////////////////////////////////////////////////////
    // // Enable pusher logging - don't include this in production
    // Pusher.logToConsole = true;
    Pusher.logToConsole = false;
    var pusher = new Pusher('55b76ba88af32c57990c', {
      cluster: 'us2',
      forceTLS: true
    });
    var editBeerChannel = pusher.subscribe('myDelBeer-evemt-channel');
    editBeerChannel.bind('delBeerFromDb-event', function(data) {
      console.log('LINE 860');
      // console.log(data.message);
      updateBottleBeerScreen(data.message);
    });
    ///////////////////////////////////////////////////////
  }

  // Load event listeners functions
  const loadEventListeners = function(){
    // Edit beerlist event
    if (document.querySelector(UISelectors.editBeerlistBtn) != null){
      document.querySelector(UISelectors.editBeerlistBtn).addEventListener('click', editBeerlistFormSubmit);
    }
    if (document.querySelector(UISelectors.submitSettingsBtn) != null){
      document.querySelector(UISelectors.submitSettingsBtn).addEventListener('click', settingsFormSubmit);
    }
    if (document.querySelector(UISelectors.editWinelistBtn) != null){
      document.querySelector(UISelectors.editWinelistBtn).addEventListener('click', editWinelistFormSubmit);
    }
    if (document.querySelector(UISelectors.addWineSubmitBtn) != null) {
      document.querySelector(UISelectors.addWineSubmitBtn).addEventListener('click', addWine);
    }
    if (document.querySelector(UISelectors.editWineSubmitBtn) != null) {
      document.querySelector(UISelectors.editWineSubmitBtn).addEventListener('click', editWine);
    }
    if (document.querySelector(UISelectors.addBeerBtn) != null) {
        document.querySelector(UISelectors.addBeerBtn).addEventListener('click', addBeerToBeerlist);
    }
    if (document.querySelector(UISelectors.delBeerBtn) != null) {
        document.querySelector(UISelectors.delBeerBtn).addEventListener('click', delBeerFromBeerlist);
    }
    if (document.querySelector(UISelectors.editBeerSubmitBtn) != null) {
        document.querySelector(UISelectors.editBeerSubmitBtn).addEventListener('click', editBeerSubmit);
    }
    if (document.querySelector(UISelectors.editOnTapNextEditorSubmitBtn) != null) {
      document.querySelector(UISelectors.editOnTapNextEditorSubmitBtn).addEventListener('click', editOnTapNextEditorSubmit);
    }
    if (document.querySelector(UISelectors.addBeerToDbSubmitBtn) != null) {
      document.querySelector(UISelectors.addBeerToDbSubmitBtn).addEventListener('click', addBeerToDbSubmit);
    }
    if (document.querySelector(UISelectors.clearDashSearch) != null) {
      document.querySelector(UISelectors.clearDashSearch).addEventListener('click', clearDashSearch);
    }
    document.addEventListener('click', (e) => {
      if (e.target.classList.contains('toggle-table')) {
        expandBeerOnDashboard(e);
      }
      if (e.target.classList.contains('untappd-add-beer-to-db')) {
        untappdAddBeerToDB(e);
      }
    });
    if (document.querySelector(UISelectors.dashboardSearchBeer) != null) {
      document.querySelector(UISelectors.dashboardSearchBeer).addEventListener('keyup', searchBeerDashboard);
    }
    if (document.querySelector(UISelectors.draftBeersTabletNavBtn) != null) {
      document.querySelector(UISelectors.draftBeersTabletNavBtn).addEventListener('click', switchTabletScreen);
    }
    if (document.querySelector(UISelectors.bottleBeersTabletNavBtn) != null) {
      document.querySelector(UISelectors.bottleBeersTabletNavBtn).addEventListener('click', switchTabletScreen);
    }
    if (document.querySelector(UISelectors.winelistMenuTabletNavBtn) != null) {
      document.querySelector(UISelectors.winelistMenuTabletNavBtn).addEventListener('click', switchTabletScreen);
    }
    if (document.querySelector(UISelectors.winelistDescriptionTabletNavBtn) != null) {
      document.querySelector(UISelectors.winelistDescriptionTabletNavBtn).addEventListener('click', switchTabletScreen);
    }
    if (document.querySelector(UISelectors.searchBeerText) != null) {
      document.querySelector(UISelectors.searchBeerText).addEventListener('keyup', searchBeerKey);
    }
    if (document.querySelector(UISelectors.searchBeerBtn) != null) {
      document.querySelector(UISelectors.searchBeerBtn).addEventListener('click', searchBeerClick);
    }
    if (document.querySelector(UISelectors.addBeerTemplateBtn) != null) {
      document.querySelector(UISelectors.addBeerTemplateBtn).addEventListener('click', addBeerscreenTemplate);
    }
    if (document.querySelector(UISelectors.delBeerTemplateBtn) != null) {
      document.querySelector(UISelectors.delBeerTemplateBtn).addEventListener('click', delBeerscreenTemplate);
    }
    if (document.querySelector(UISelectors.beerscreenDisplayId) != null) {
      document.querySelector(UISelectors.beerscreenDisplayId).addEventListener('change', getBeerlistScreen);
    }
    document.addEventListener('mousemove', (e) => {
      if (document.querySelector(UISelectors.screenDisplay) != null) {
        displayScreenNavBtns();
      }
    });
    if (document.querySelector(UISelectors.beersDisplayNavPrev) != null) {
      document.querySelector(UISelectors.beersDisplayNavPrev).addEventListener('click', changeToPrevBeersDisplayScreen);
    }
    if (document.querySelector(UISelectors.beersDisplayNavNext) != null) {
      document.querySelector(UISelectors.beersDisplayNavNext).addEventListener('click', changeToNextBeersDisplayScreen);
    }
  }

    // Edit beer list submit
    const editBeerlistFormSubmit = function(e) {
      console.log('CLICK EDIT BEERLIST FORM SUBMIT');
      const editBeerlistForm = document.querySelector(UISelectors.editBeerlistForm);
      // console.log(editBeerlistForm);
      (function(loadPusher){
        // console.log(loadPusher);
        editBeerlistForm.submit();
        loadPusher();
      })(loadPusher);
      // e.preventDefault();
    }

      // Settings form submit
    const settingsFormSubmit = function(e) {
      console.log('CLICK SETTIINGS BUTTON');
      const settingsForm = document.querySelector(UISelectors.settingsForm);
      (function(loadPusher){
          settingsForm.submit();
          loadPusher();
      })(loadPusher);
      e.preventDefault();
    }

    const editWinelistFormSubmit = function(e) {
      console.log('CLICK EDIT WINELIST FORM SUBMIT');
      const editWinelistForm = document.querySelector(UISelectors.editWinelistForm);
      (function(loadWinePusher){
        editWinelistForm.submit();
        loadWinePusher();
      })(loadWinePusher);
      e.preventDefault();
    }
    const addWine = function(e) {
      console.log('CLICK ADD WINE TO WINELIST');
      const addWineForm = document.querySelector(UISelectors.addWineForm);
      (function(addWinePusher){
        addWineForm.submit();
        // console.log("ADDWINEPUSHER()");
        addWinePusher();
        console.log("LINE 598");
      })(addWinePusher);
      e.preventDefault();
    }
    const editWine = function(e) {
      console.log('CLICK EDIT WINE');
      const editWineForm = document.querySelector(UISelectors.editWineForm);
      editWineForm.submit();
      loadWinePusher();
      e.preventDefault();
    }

    async function addBeerToBeerlist(e) {
      // console.log('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~');
      // console.log('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~');
      console.log('CLICK PLUS BUTTON TO ADD BEER TO LISTS');
      // console.log('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~');
      // console.log('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~');
      let userNameScreenId = UserCtrl.callGetUserNameFromURL();
      // returns { "userName": userName, "screenNumber": screenNumber }
      console.log(userNameScreenId);

      // add new beer to listCurrent DB
      // find id of first beer of current user
      let listData = await BeerCtrl.callFetchBeerhistoryList(userNameScreenId);
      console.log(listData);
      let listHistory = listData.beerlist;
      console.log(listHistory);
      let id_history = listHistory[0].id[0];
      // console.log(id_history);

      // get the current screenId from the select to query for the current_list of beers
      let beerscreenDisplayId = document.querySelector(UISelectors.beerscreenDisplayId).value;
      console.log(beerscreenDisplayId);
      userNameScreenId.screenNumber = beerscreenDisplayId;
      console.log(userNameScreenId);
      // get the current beerlist for user and screenId
      let currentBeerlist = await BeerCtrl.callFetchCurBeerlist(userNameScreenId);
      // let currentBeerlist = await BeerCtrl.callFetchCurBeerlist( {"user_id": userNameScreenId, "beerscreenDisplayId": beerscreenDisplayId} );

      console.log(currentBeerlist);
      // console.log(currentBeerlist.length + 1);
      let id_dropdown = currentBeerlist.length + 1;
      // console.log(id_dropdown);

      let newBeer = {
        "id_history": id_history,
        "id_on_next": id_history,
        "id_dropdown": id_dropdown,
        "beer_screen_id": beerscreenDisplayId,
        "venue_db_id": ""
      }
      console.log(newBeer);
      // Add new beer to list_current table in DB
      BeerCtrl.callFetchAddBeerToDB(newBeer);
      // use pusher to update UI on all screens with the new beer
      UpdateCtrl.callFetchAddUpdateScreenUI();
      e.preventDefault();
    }

    async function delBeerFromBeerlist(e) {
      console.log('CLICK MINUS BUTTON TO DELETE BEER FROM LISTS');
      let userNameScreenId = UserCtrl.callGetUserNameFromURL();
      let screenNumber = document.querySelector(UISelectors.beerscreenDisplayId).value;
      userNameScreenId.screenNumber = screenNumber;
      userNameScreenId.venueName = "";
      userNameScreenId.userId = "";
      userNameScreenId.userName = "";
      console.log(userNameScreenId);
      let currentBeerlist = await BeerCtrl.callFetchCurBeerlist(userNameScreenId);
      console.log(currentBeerlist);
      let beerIdToBeDeleted = currentBeerlist.length;
      console.log(beerIdToBeDeleted);
      let dataToSend = {
        "userNameScreenId": userNameScreenId,
        "beerIdToBeDeleted": beerIdToBeDeleted,
      };
      let beerData = await BeerCtrl.callFetchDeleteBeerFromCurrentListDb(dataToSend);
      console.log(beerData);

      // // get the ID of the last beer in the beerlist to be removed from the DB
      // // deletes last beer of the beerlist on the edit_beer_list UI
      let beer_id = UICtrl.callDeleteBeerFromListEditor(beerData.userNameScreenId.userId);
      // let res = await UserCtrl.callFetchUserData(userNameScreenId);
      // deletes the beer from the DB using the ID of the beer return deleting on the UI
      // UpdateCtrl.callFetchDeleteUpdateScreenUI();
      e.preventDefault();
    }

    async function editOnTapNextEditorSubmit() {
      console.log('SUBMITING ON TAP NEXT EDITOR');
      const onTapNextEditorForm = document.querySelector(UISelectors.editOnTapNextEditorForm);
      onTapNextEditorForm.submit();
      // let data = await BeerCtrl.callFetchAllTotalCurrentNextLists();
      // console.log(data);
    }

    const addBeerToDbSubmit = function(e) {
      console.log('SUBMITTING ON NEW BEER TO DB');
      const addBeerToDbForm = document.querySelector(UISelectors.addBeerToDbForm);
      (function(addBeerToDbPusher){
        addBeerToDbForm.submit();
        addBeerToDbPusher();
      })(addBeerToDbPusher);
      e.preventDefault();
    }

    const editBeerSubmit = function(e) {
      console.log('EDITING BEER NOW');
      const editBeerForm = document.querySelector(UISelectors.editBeerForm);
      (function(editBeerToDbPusher){
        editBeerForm.submit();
        editBeerToDbPusher();
      })(editBeerToDbPusher);
      e.preventDefault();
    }

    const clearDashSearch = async function(e) {
      // **clear the search for the dashboard and reset the dashboard table list
      let clearDashSearchBeerBtn = document.querySelector(UISelectors.dashboardSearchBeer);
      let dashboardSearchBeerInput = document.querySelector(UISelectors.dashboardSearchBeer);
      let dashboardBeerInfo = document.querySelector(UISelectors.dashboardBeerInfo);
      // clear dashboard search input
      let getValue = dashboardSearchBeerInput.value;
      // console.log(getValue);
      // clear the dashboard beerlist to start a new search
      // console.log(dashboardBeerInfo);
      dashboardBeerInfo.innerHTML = '';

      // repopulate/repaint beerlist table on beer_dashboard.html
      let beerlist = await BeerCtrl.callFetchBeerhistoryList();
      UICtrl.callRepaintBeerlistDashboard(beerlist);

      // clear the text input to start a new search
      console.log('CLEARING SEARCH BAR NOW');
      dashboardSearchBeerInput.value = '';
      // set focus to the text input on beer_dashboard.html
      dashboardSearchBeerInput.focus();
      e.preventDefault();
    }

    // expand a beerlist item on the beer_dashboard
    const expandBeerOnDashboard = function(e) {
      console.log('TOGGLE-TABLE');
      e.target.parentElement.nextElementSibling.firstElementChild.classList.toggle('d-none');
    }

    // search the current beers on the dashboard for a particular beer
    const searchBeerDashboard = function(e) {
      let beerDashboardTableRows = document.querySelectorAll(UISelectors.dashboardTableRowName);
      console.log('SEARCHING BEERLIST ON DASHBOARD');
      // console.log(e);
      const userText = e.target.value.toLowerCase();
      if (userText !== '') {
        beerDashboardTableRows.forEach(tableRow => {
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
      } else {
        beerDashboardTableRows.forEach(tableRow => {
          tableRow.classList.remove('d-none');
        });
      }
    }

    // tablet menuscreen switch screens without being logged in.
    const switchTabletScreen = (e) => {
      console.log('SWITCH TABLET SCREEN NOW');
      // get the clicked button id
      let targetId = e.target.id;
      // split the id to get the new page
      let targetPage = targetId.split('-').slice(0,2).join('_');
      // console.log(targetPage);

      // get the current window url
      let currentWindowURL = window.location.href;
      // console.log(currentWindowURL);
      // split the current window url to replace with target url info
      currentWindowSplitURL = currentWindowURL.split('/');
      // console.log(currentWindowSplitURL);

      // let currentButton = currentWindowSplitURL[3];
      // console.log(currentButton);

      // replace third element of url with the target button id to create new url
      currentWindowSplitURL[3] = targetPage;
      // create new url
      let newPage = currentWindowSplitURL.join('/');
      // console.log(newPage);
      // redirect to new page
      window.location.replace(newPage);
    }

    // search untappd for beers with enter key
    const searchBeerKey = async (e) => {
      // Get input text from user
      const userSearchUntappdText = e.target.value;
      // console.log(userSearchUntappdText);
      // get the event of the key pushed
      // looking for keyCode 13 which is "enter" key
      // if keyCode === 13 process user text input and query Untappd DB
      // console.log(e.keyCode);
      if (e.keyCode === 13) {
        // process user text input and search Untappd DB
        if (userSearchUntappdText !== '') {
          const untappd = UntappdCtrl;
          let beerData = await untappd.callLoadData(userSearchUntappdText);
          // console.log(beerData);
          let userNameScreenId = UserCtrl.callGetUserNameFromURL();
          // console.log(userNameScreenId);
          let userData = await UserCtrl.callFetchUserData(userNameScreenId);
          // console.log(userData);

          let untappdInfo = { "beerData": beerData, "userData": userData }

          // console.log(untappdInfo);
          // load data into the UI
          let untappdResultsTemplate = UICtrl;
          untappdResultsTemplate.callPaintUntappdSearchResultsList(untappdInfo);
        } else {
          // clear the list of searched beers
        }
        e.preventDefault();
      }
    }
    // search untappd for beers with click
    const searchBeerClick = async (e) => {
      console.log("SEARCH BEER FROM UNTAPPD - TO ADD TO DB");
      let userSearchUntappdText = document.querySelector(UISelectors.searchBeerText).value;
      if (userSearchUntappdText !== '') {
        const untappd = UntappdCtrl;
        let beerData = await untappd.callLoadData(userSearchUntappdText);
        // console.log(beerData);
        let userNameScreenId = UserCtrl.callGetUserNameFromURL();
        // console.log(userNameScreenId);
        let userData = await UserCtrl.callFetchUserData(userNameScreenId);
        // console.log(userData);

        let untappdInfo = { "beerData": beerData, "userData": userData }

        // console.log(untappdInfo);
        // load data into the UI
        let untappdResultsTemplate = UICtrl;
        untappdResultsTemplate.callPaintUntappdSearchResultsList(untappdInfo);
      } else {
        // clear the list of searched beers
      }
      e.preventDefault();
    }

    // add all or one of the beers from the untapd search list
    const untappdAddBeerToDB = async (e) => {
      // console.log(e);
      // get beerID from UI
      const uictrl = UICtrl;
      let beerInfo = uictrl.callGetBeerIdFromUI(e);
      // console.log(beerInfo);
      // use untappd to get beer and brewery info with beerID
      let untappd = UntappdCtrl;
      let newBeer = await untappd.callGetSingleBeerById(beerInfo.id);
      let newBeerInfo = { "beer": newBeer, "draftBottleSelection": beerInfo.selectedRadioVal }
      // create beer object and add draft-bottle selection
      let newBeerObj = BeerCtrl.callCreateNewBeerObj(newBeerInfo);
      // console.log(newBeerObj);
      // add beer to DB
      BeerCtrl.callFetchAddNewBeerToDB(newBeerObj);

      e.preventDefault();
    }

    const addBeerscreenTemplate = async (e) => {
      console.log('addBeerscreenTemplate');
      // get number of screens current in the UI to increment and add to UI
      let displayScreenIds = UICtrl.callAddToEditBeerlistScreenSelect();
      // send number of screens to database to init new setting options, new current_list, new ticker
      // call route to add this to the database
      let res = await BeerCtrl.callSendScreenSettingsInfoToDb(displayScreenIds);
      res.venue_db_id = res.id;
      let userNameScreenId = await getUserInfo(res);
      let displayRes = await getScreenInfo(userNameScreenId);
      UICtrl.callRepaintBeerlistEditor(displayRes);
      e.preventDefault();
    }

    const delBeerscreenTemplate = async (e) => {
      console.log('delBeerscreenTemplate');
      // get current number of beer display screens/ beersettings
      let displayScreenIds = UICtrl.callDelFromEditBeerlistScreenSelect();
      // console.log(displayScreenIds);
      if (displayScreenIds > 1) {
        // remove screenId row number from database tables list_current & beerscreen_settings
        let res = await BeerCtrl.callRemoveScreenSettingsInfoFromDb(displayScreenIds);
        res.venue_db_id = res.id;
        let userNameScreenId = await getUserInfo(res);
        let displayRes = await getScreenInfo(userNameScreenId);
        UICtrl.callRepaintBeerlistEditor(displayRes);
      }
      e.preventDefault();
    }


    //edit beerlist switching screens edit list
    const getBeerlistScreen = async (e) => {
      console.log('SWITCHING BEERSCREEN EDITORS NOW');
      let screenId = e.target.value;
      // console.log(screenId);
      let userIdEl = e.target.parentElement.parentElement.parentElement.nextElementSibling.nextElementSibling.id;
      let userId = userIdEl.split("-")[2];
      // console.log(userId);
      let userNameScreenId = {};
      userNameScreenId.screenNumber = screenId;
      userNameScreenId.userId = userId;
      // console.log(userNameScreenId);

      // switch from a screen to selected screen
      // update edit_beer_list
      // console.log("Query fetchCurBeerlist");
      // console.log("Query fetchNextBeerlist");
      // console.log("Query fetchBeerhistoryList");
      // console.log("Query fetchTickerInfo");
      // console.log("repaint Edit beerlist")
      let displayData = await getScreenInfo(userNameScreenId);
      console.log(displayData);
      UICtrl.callRepaintBeerlistEditor(displayData);
      e.preventDefault();
    }

    const displayScreenNavBtns = () => {
      let prevBtn = document.querySelector(UISelectors.beersDisplayNavPrev);
      let nextBtn = document.querySelector(UISelectors.beersDisplayNavNext);
      prevBtn.classList.remove("d-none");
      nextBtn.classList.remove("d-none");
      prevBtn.classList.add("fade-in");
      nextBtn.classList.add("fade-in");
      setTimeout(function(){
        prevBtn.classList.add("d-none");
        nextBtn.classList.add("d-none");
        prevBtn.classList.remove("fade-in");
        nextBtn.classList.remove("fade-in");
      },10000);
    }

    // on beers_display_screen switch previous screen accordingly
    const changeToPrevBeersDisplayScreen = async (e) => {
      // console.log(e.target);
      // get the current window URL
      let currentWindowURL = window.location.href;
      console.log(currentWindowURL);
      // split the curren window url to replace with the target url info
      currentWindowSplitURL = currentWindowURL.split('/');
      console.log(currentWindowSplitURL);
      let currentPage = currentWindowSplitURL[3];
      let currentUser = currentWindowSplitURL[4];
      let currentScreenNumber = currentWindowSplitURL[5];
      console.log(`${currentPage} - ${currentUser} - ${currentScreenNumber}`);
      // replace fifth element of url with the previous screen number
      if (currentScreenNumber > 1) {
        currentScreenNumber--;
      } else {
        let screenNumberArr = await ScreenSettingsCtrl.callFetchNumberOfBeerScreens();
        let screenNumberLength = screenNumberArr.length;
        currentScreenNumber = screenNumberLength;
      }
      let targetScreenNumber = currentScreenNumber;
      console.log(targetScreenNumber);
      currentWindowSplitURL[5] = targetScreenNumber;
      console.log(currentWindowSplitURL);
      // create new URL
      let newPage = currentWindowSplitURL.join('/');
      console.log(newPage);
      // redirect to new page
      window.location.replace(newPage);
    }
    // on beers_display_screen switch to next screen accordingly
    const changeToNextBeersDisplayScreen = async (e) => {
      // console.log(e.target);
      // get the current window URL
      let currentWindowURL = window.location.href;
      console.log(currentWindowURL);
      // split the curren window url to replace with the target url info
      currentWindowSplitURL = currentWindowURL.split('/');
      console.log(currentWindowSplitURL);
      let currentPage = currentWindowSplitURL[3];
      let currentUser = currentWindowSplitURL[4];
      let currentScreenNumber = currentWindowSplitURL[5];
      console.log(`${currentPage} - ${currentUser} - ${currentScreenNumber}`);
      // replace fifth element of url with the previous screen number
      let screenNumberArr = await ScreenSettingsCtrl.callFetchNumberOfBeerScreens();
      let screenNumberLength = screenNumberArr.length;
      if (currentScreenNumber < screenNumberLength) {
        currentScreenNumber++;
      } else {
        currentScreenNumber = 1;
      }
      let targetScreenNumber = currentScreenNumber;
      console.log(targetScreenNumber);
      currentWindowSplitURL[5] = targetScreenNumber;
      console.log(currentWindowSplitURL);
      // create new URL
      let newPage = currentWindowSplitURL.join('/');
      console.log(newPage);
      // redirect to new page
      window.location.replace(newPage);
    }

  // Public methods
  return {
    init: function(){
      loadUpdatePusher();
      loadPusher();
      addBeerToDbPusher();
      editBeerToDbPusher();
      delBeerFromDbPusher();
      loadWinePusher();

      // Show flash message div and then hide after 2.5 seconds
      UICtrl.callHideFlashMsg();
      // BeerCtrl.callFetchCurrentBeerList(UICtrl.callUpdateDisplayScreen);
      // WineCtrl.callFetchCurrentWinelist(UICtrl.callUpdateWineTabletScreen);
      // Call load event listeners function
      loadEventListeners();
      // console.log("TRYING TO INITIALIZE THE SCREENS!!!!!!!!!")
      initScreens({"updated":"True"});
    }
  }

})(UserCtrl, UpdateCtrl, BeerCtrl, UntappdCtrl, TickerCtrl, WineCtrl, EventCtrl, ScreenSettingsCtrl, UICtrl);

// Initialize App
App.init();
