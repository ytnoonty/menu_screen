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

  async function fetchUserData() {
    // console.log("FETCHING USER DATA");
    const fetchResponse = await fetch('/_logged_in_user_data');
    const data = await fetchResponse.json();
    return data;
  }

  return {
    callFetchUserData: function() {
      return fetchUserData();
    },
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
    console.log(data);
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

  async function fetchBeerhistoryList() {
    const fetchResponse = await fetch('/_getTotBeerlist');
    const data = await fetchResponse.json();
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

  const fetchTotBeerlist = function(template) {
    const fetchBeers = function(template) {
      fetch('/_getTotBeerlist')
      .then((res) => res.json())
      .then((data) => {
        template(data);
      })
    }
    fetchBeers(template);
  }

  async function fetchCurBeerlist() {
    const fetchResponse = await fetch('/_getCurBeerlist');
    const data = await fetchResponse.json();
    return data;
  }

  async function fetchNextBeerlist() {
    const fetchResponse = await fetch('/_getNextBeerlist');
    const data = await fetchResponse.json();
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

  const fetchDeleteBeerFromDb = function(id) {
    const deleteBeerFromDb = function(beer) {
      console.log(beer);
      fetch('/_delete_beer_from_list', {
        method: "POST",
        credentials: "include",
        body: JSON.stringify(beer),
        cache: "no-cache",
        headers: new Headers({
          "content-type": "application/json"
        })
      })
      .then((res) => res.json())
      .then((data) => console.log(data))
    }
    deleteBeerFromDb(id);
  }

  async function fetchAllTotalCurrentNextLists() {
    const fetchResponse = await fetch('/_getAllTotalCurrentNextLists');
    const data = await fetchResponse.json();
    console.log(data);
    return data;
  }

  async function fetchBottleBeerlist(template) {
    const fetchResponse = await fetch('/_getBottleBeerlist');
    const data = await fetchResponse.json();
    template(data);
  }

  // Public methods
  return {
    getItems: function(){
      return data.items;
    },
    logData: function(){
      return data;
    },
    callFetchBeerhistoryList: function () {
      return fetchBeerhistoryList();
    },
    callFetchCurrentBeerList: function(template) {
      fetchCurrentBeerList(template);
    },
    callFetchTotBeerlist: function(template) {
      fetchTotBeerlist(template);
    },
    callFetchCurBeerlist: function() {
      return fetchCurBeerlist();
    },
    callFetchNextBeerlist: function() {
      return fetchNextBeerlist();
    },
    callFetchAddBeerToDB: function(beer_id) {
      fetchAddBeerToDB(beer_id);
    },
    callFetchDeleteBeerFromDb: function(beer_id) {
      console.log(beer_id);
      fetchDeleteBeerFromDb(beer_id);
    },
    callFetchAllTotalCurrentNextLists: function() {
      return fetchAllTotalCurrentNextLists();
    },
    callFetchBottleBeerlist: function(template) {
      fetchBottleBeerlist(template);
    }
  }

})();
////////////////////////////////////////////////////////////////////////////////
// END BEER CONTROLLER
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
        console.log(data);
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
  async function getCurrentEventlist () {
    const fetchResponse = await fetch('/_get_event_current_list');
    const data = await fetchResponse.json();
    return data;
  }

  return {
    callGetCurrentEventlist: function() {
      return getCurrentEventlist();
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
  async function fetchScreenSettings() {
    const fetchResponse = await fetch('/_get_screen_settings');
    const data = await fetchResponse.json();
    return data;
  }

  return {
    callFetchScreenSettings: async function() {
      return await fetchScreenSettings();
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
  }

  // flash message dissapear after 2.5 seconds
  const hideFlashMsg = function() {
    let flashMsgDiv = document.querySelector(UISelectors.flashMsgDiv);
    setTimeout(() => {
      flashMsgDiv.style.display = 'none';
    },2500);
  }

  const loadBeerlist = function() {
    console.log('LOAD BEERLIST');
  }

  const updateDisplayScreen = function(displayData) {
    console.log("**************************************************************************************");
    console.log("UPDATE DISPLAY SCREEN");
    console.log("**************************************************************************************");
    console.log(displayData);
    const { screenSettings } = displayData;
    console.log(screenSettings.templateName);
    const beerscreenTemplate = new BeerTemplate;
    const eventscreenTemplate = new EventTemplate;
    let templateName = screenSettings.templateName;
    if (templateName == '2 Columns, Name, Style, ABV, IBU') {
      console.log("**************************************************************************************");
      console.log('IN THE DEFAULT TEMPLATE');
      console.log("**************************************************************************************");
      beerscreenTemplate.defaultTemplate(displayData);
    } else if (templateName == '2 Columns, Name, ABV, IBU') {
      console.log("**************************************************************************************");
      console.log('IN THE DEFAULT TEMPLATE');
      console.log("**************************************************************************************");
      beerscreenTemplate.defaultTemplate(displayData);
    } else if (templateName == '2 Columns, Name, Style, ABV'){
      console.log('IN THE 2sna TEMPLATE');
      beerscreenTemplate.twoColNSAITemplate(displayData);
    } else if (templateName == '2 Columns, Name, Style'){
      console.log('IN THE 2sn TEMPLATE');
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
    console.log(displayData);
    const { beerlist } = displayData;
    // console.log('IN THE updateBottleBeersTabletScreen');
    const beersprintTemplate = new BeerTemplate;
    beersprintTemplate.bottleBeersTabletScreenTemplate(displayData);
    // beersprintTemplate.bottleBeersTabletScreenTemplate(beers);
  }

  const updateWineTabletScreen = (displayData) => {
    console.log(displayData);
    const wineScreenTabletTemplate = new WineTemplate;
    wineScreenTabletTemplate.wineTabletTemplate(displayData);
  }
  const updateWineDescriptionsTabletScreen = (displayData) => {
    console.log(displayData);
    const wineScreenwineDescriptionsTabletTemplateTabletTemplate = new WineTemplate;
    wineScreenwineDescriptionsTabletTemplateTabletTemplate.wineDescriptionsTabletTemplate(displayData);
  }

  const addBeerToListEditor = (data) => {
      const addBeerToListTemplate = new BeerTemplate;
      addBeerToListTemplate.addBeerToListEditorTemplate(data);
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
  }
})();
////////////////////////////////////////////////////////////////////////////////
// END UICtrl
////////////////////////////////////////////////////////////////////////////////

////////////////////////////////////////////////////////////////////////////////
// App Controller
////////////////////////////////////////////////////////////////////////////////
const App = (function(UserCtrl, UpdateCtrl, BeerCtrl, WineCtrl, EventCtrl, ScreenSettingsCtrl, UICtrl){
  // Get UI Selectors
  const UISelectors = UICtrl.getSelectors();

  async function addUpdateScreens(data) {
    console.log("///////////////////////////////////////////////////////////////////////////");
    console.log("ADD UPDATE SCREENS");
    console.log(data.venue_db_id);
    console.log("///////////////////////////////////////////////////////////////////////////");

    // // add new beer to current screen edit_beer_list
    // BeerCtrl.callFetchTotBeerlist(UICtrl.callAddBeerToListEditor);

    // query the DB for the current beerlist
    let currentBeers = await BeerCtrl.callFetchCurBeerlist();
    // console.log(currentBeers);
    // query the DB for the next beerlist
    let nextBeers = await BeerCtrl.callFetchNextBeerlist();
    // console.log(nextBeers);
    // query the DB for the list history
    let beerslistTotal = await BeerCtrl.callFetchBeerhistoryList();
    // console.log(beerslistTotal);
    // query the DB for the events
    let events = await EventCtrl.callGetCurrentEventlist();
    // let userData = await UserCtrl.callFetchUserData();
    let screenSettings = await ScreenSettingsCtrl.callFetchScreenSettings();
    // console.log(screenSettings);
    userData = data.venue_db_id;
    // console.log(userData);
    let onNext;
    let displayData = {};

    displayData = {
      "currentBeers": currentBeers,
      "nextBeers": nextBeers,
      "beerslistTotal": beerslistTotal,
      "events": events,
      "screenSettings": screenSettings,
      "userSettings": { "venue_db_id": userData }
    }


    // console.log(displayData);
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
  }

  async function deleteUpdateScreens(data) {
    console.log("///////////////////////////////////////////////////////////////////////////");
    console.log("DELETE UPDATE SCREENS");
    console.log("///////////////////////////////////////////////////////////////////////////");

    // delete beer from current screen from edit_beer_list
    // function call to delete


    // query the DB for the current beerlist
    let currentBeers = await BeerCtrl.callFetchCurBeerlist();
    // console.log(currentBeers);
    // query the DB for the next beerlist
    let nextBeers = await BeerCtrl.callFetchNextBeerlist();
    // console.log(nextBeers);
    // query the DB for the list history
    let beerslistTotal = await BeerCtrl.callFetchBeerhistoryList();
    // console.log(beerslistTotal);
    // query the DB for the events
    let events = await EventCtrl.callGetCurrentEventlist();
    let userData = await UserCtrl.callFetchUserData();
    let screenSettings = await ScreenSettingsCtrl.callFetchScreenSettings();
    // console.log(screenSettings);
    userData = userData.id[0];
    // console.log(userData);
    let onNext;
    let displayData = {};

    displayData = {
      "currentBeers": currentBeers,
      "nextBeers": nextBeers,
      "beerslistTotal": beerslistTotal,
      "events": events,
      "screenSettings": screenSettings,
      "userSettings": { "venue_db_id": userData }
    }
    // console.log(displayData);
    // // update all screens
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

  }


  async function initScreens(data) {
    // console.log(data);
    if (data !== undefined) {
      if (data.updated) {

        let currentBeers = await BeerCtrl.callFetchCurBeerlist();
        let nextBeers = await BeerCtrl.callFetchNextBeerlist();
        // console.log(nextBeers);
        let beerslistTotal = await BeerCtrl.callFetchBeerhistoryList();
        let events = await EventCtrl.callGetCurrentEventlist();
        let userData = await UserCtrl.callFetchUserData();
        let screenSettings = await ScreenSettingsCtrl.callFetchScreenSettings();
        console.log(screenSettings);
        userData = userData.id[0];
        // console.log(userData);
        let onNext;

        currentBeers.forEach(beer => {
          onNext = beer.id_on_next;
          nextBeers.push(onNext);
        });

        // console.log("onNext: " + onNext + "nextBeers: " + nextBeers);

        let displayData = {
          "currentBeers": currentBeers,
          "nextBeers": nextBeers,
          "beerslistTotal": beerslistTotal,
          "events": events,
          "screenSettings": screenSettings,
          "userSettings": { "venue_db_id": userData }
        }
        console.log(displayData);

        UICtrl.callUpdateDisplayScreen(displayData);
        UICtrl.callUdpateDraftBeersPrintScreen(displayData);
        UICtrl.callUpdateDraftBeersTabletScreen(displayData);

        UICtrl.callAddBeerOnTapNextDisplay(displayData);
        UICtrl.callAddBeerOnTapNextEditor(displayData);

        // update bottle beer list asynconously
        UICtrl.callUpdateBottleBeersTabletScreen(displayData);
        // BeerCtrl.callFetchBottleBeerlist(UICtrl.callUpdateBottleBeersTabletScreen);
      }
    }
  }





  const initWineScreens = (data) => {
    if (data !== undefined) {
        console.log(data.updated);
        if (data.updated == true) {
            WineCtrl.callFetchCurrentWinelist(UICtrl.callUpdateWineTabletScreen);
            WineCtrl.callFetchCurrentWinelist(UICtrl.callUpdateWineDescriptionsTabletScreen);
        }
    }
  }
  const editWineScreens = (data) => {
    if (data !== undefined) {
        console.log(data.updated);
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
      console.log(data.updated);
      if (data.updated == true) {
        console.log("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&");
        console.log("DATA CAN AND WILL BE UPDATED NOW!")
        console.log("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&");
      }
    }
  }

  async function updateBottleBeerScreen (data) {
    // console.log(data);
    if (data !== undefined) {
      // console.log(data.updated);
      if (data.updated == true) {
        // console.log("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&");
        // console.log("BOTTLE BEER CAN AND WILL BE UPDATED NOW!")
        // console.log("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&");
        // call to fetch bottle beerlist
        // update user interface for bottle beerlist screen
        let currentBeers = await BeerCtrl.callFetchCurBeerlist();
        let nextBeers = await BeerCtrl.callFetchNextBeerlist();
        let beerslistTotal = await BeerCtrl.callFetchBeerhistoryList();
        // query the DB for the events
        let events = await EventCtrl.callGetCurrentEventlist();
        let userData = await UserCtrl.callFetchUserData();
        let screenSettings = await ScreenSettingsCtrl.callFetchScreenSettings();
        let onNext;
        userData = userData.id[0];
        // console.log(nextBeers);

        currentBeers.forEach(beer => {
          onNext = beer.id_on_next;
          nextBeers.push(onNext);
        });
        // console.log("onNext: " + onNext + "nextBeers: " + nextBeers);

        let displayData = {
          "currentBeers": currentBeers,
          "nextBeers": nextBeers,
          "beerslistTotal": beerslistTotal,
          "events": events,
          "screenSettings": screenSettings,
          "userSettings": { "venue_db_id": userData }
        }
        // console.log(displayData);

        UICtrl.callUpdateDisplayScreen(displayData);
        UICtrl.callUdpateDraftBeersPrintScreen(displayData);
        UICtrl.callUpdateDraftBeersTabletScreen(displayData);
        UICtrl.callAddBeerOnTapNextDisplay(displayData);
        // update bottle beer list asynconously
        UICtrl.callUpdateBottleBeersTabletScreen(displayData);
        // BeerCtrl.callFetchBottleBeerlist(UICtrl.callUpdateBottleBeersTabletScreen);
      }
    }
  }

  // load update pusher
  const loadUpdatePusher = function() {
    ///////////////////////////////////////////////////////
    // // Enable pusher logging - don't include this in production
    Pusher.logToConsole = true;
    var addPusher = new Pusher('55b76ba88af32c57990c', {
      cluster: 'us2',
      forceTLS: true
    });
    var addChannel = addPusher.subscribe('my-update-channel');
    addChannel.bind('new-addUpdate-event', function(data) {
      console.log(data.message);
      addUpdateScreens(data.message);
    });
    ///////////////////////////////////////////////////////

    ///////////////////////////////////////////////////////
    // // Enable pusher logging - don't include this in production
    Pusher.logToConsole = true;
    var deletePusher = new Pusher('55b76ba88af32c57990c', {
      cluster: 'us2',
      forceTLS: true
    });
    var deleteChannel = deletePusher.subscribe('my-update-channel');
    deleteChannel.bind('new-deleteUpdate-event', function(data) {
      // console.log(data);
      deleteUpdateScreens(data);
    });
    ///////////////////////////////////////////////////////












    ///////////////////////////////////////////////////////
    // // Enable pusher logging - don't include this in production
    Pusher.logToConsole = true;
    var nextPusher = new Pusher('55b76ba88af32c57990c', {
      cluster: 'us2',
      forceTLS: true
    });
    var updateNextChannel = nextPusher.subscribe('my-update-channel');
    updateNextChannel.bind('new-nextUpdate-event', function(data) {
      // update the next lists
      console.log(data.message);
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
    Pusher.logToConsole = true;
    var pusher = new Pusher('55b76ba88af32c57990c', {
      cluster: 'us2',
      forceTLS: true
    });
    var channel = pusher.subscribe('my-event-channel');
    channel.bind('new-event', function(data) {
      console.log(data);
      initScreens(data.message);
    });
    ///////////////////////////////////////////////////////
  }

  const loadWinePusher = function() {
    ///////////////////////////////////////////////////////
    // // Enable pusher logging - don't include this in production
    Pusher.logToConsole = true;
    var pusher = new Pusher('55b76ba88af32c57990c', {
      cluster: 'us2',
      forceTLS: true
    });
    var addChannel = pusher.subscribe('wine-event-channel');
    addChannel.bind('add-wine-event', function(data) {
      console.log(data.message);
      initWineScreens(data.message);
    });

    var editChannel = pusher.subscribe('wine-event-channel');
    editChannel.bind('edit-wine-event', function(data) {
      console.log(data.message);
      editWineScreens(data.message);
    });
    ///////////////////////////////////////////////////////
  }

  const addWinePusher = function() {
    ///////////////////////////////////////////////////////
    // // Enable pusher logging - don't include this in production
    Pusher.logToConsole = true;
    var pusher = new Pusher('55b76ba88af32c57990c', {
      cluster: 'us2',
      forceTLS: true
    });
    var channel = pusher.subscribe('wine-event-channel');
    channel.bind('add-wine-event', function(data) {
      console.log(data.message);
        initWineScreens(data.message);
    });
    ///////////////////////////////////////////////////////
  }

  // const loadBeerPusher = function() {
  //   ///////////////////////////////////////////////////////
  //   // // Enable pusher logging - don't include this in production
  //   Pusher.logToConsole = true;
  //   var pusher = new Pusher('55b76ba88af32c57990c', {
  //     cluster: 'us2',
  //     forceTLS: true
  //   });
  //   var channel = pusher.subscribe('beer-event-channel');
  //   channel.bind('new-beer-event', function(data) {
  //       console.log(data.message);
  //       updateBeerScreen(data.message);
  //   });
  //   ///////////////////////////////////////////////////////
  // }





  const addBeerToDbPusher = function() {
    ///////////////////////////////////////////////////////
    // // Enable pusher logging - don't include this in production
    Pusher.logToConsole = true;
    var pusher = new Pusher('55b76ba88af32c57990c', {
      cluster: 'us2',
      forceTLS: true
    });
    var addBeerChannel = pusher.subscribe('myAddBeer-event-channel');
    addBeerChannel.bind('addBeerToDb-event', function(data) {
      console.log('LINE 826');
      console.log(data.message);
      updateBottleBeerScreen(data.message);
    });
    ///////////////////////////////////////////////////////
  }
  const editBeerToDbPusher = function() {
    ///////////////////////////////////////////////////////
    // // Enable pusher logging - don't include this in production
    Pusher.logToConsole = true;
    var pusher = new Pusher('55b76ba88af32c57990c', {
      cluster: 'us2',
      forceTLS: true
    });
    var editBeerChannel = pusher.subscribe('myEditBeer-evemt-channel');
    editBeerChannel.bind('editBeerToDb-event', function(data) {
      console.log('LINE 842');
      console.log(data.message);
      updateBottleBeerScreen(data.message);
    });
    ///////////////////////////////////////////////////////
  }

  const delBeerFromDbPusher = function() {
    ///////////////////////////////////////////////////////
    // // Enable pusher logging - don't include this in production
    Pusher.logToConsole = true;
    var pusher = new Pusher('55b76ba88af32c57990c', {
      cluster: 'us2',
      forceTLS: true
    });
    var editBeerChannel = pusher.subscribe('myDelBeer-evemt-channel');
    editBeerChannel.bind('delBeerFromDb-event', function(data) {
      console.log('LINE 860');
      console.log(data.message);
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
  }














    // Edit beerlist submit
    const editBeerlistFormSubmit = function(e) {
      console.log('CLICK EDIT BEERLIST FORM SUBMIT');
      const editBeerlistForm = document.querySelector(UISelectors.editBeerlistForm);
      console.log(editBeerlistForm);
      (function(loadPusher){
        // console.log(loadPusher);
        loadPusher();
        editBeerlistForm.submit();
      })(loadPusher);
      e.preventDefault();
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
        console.log("ADDWINEPUSHER()");
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
      console.log('CLICK PLUS BUTTON TO ADD BEER TO LISTS');
      // add new beer to listCurrent DB
      // find id of first beer of current user
      let listData = await BeerCtrl.callFetchBeerhistoryList();
      let listHistory = listData.beerlist;
      let id_history = listHistory[0].id[0];
      // console.log(id_history);
      // get the current beerlist
      let currentBeerlist = await BeerCtrl.callFetchCurBeerlist();
      // console.log(currentBeerlist);
      // console.log(currentBeerlist.length + 1);
      let id_dropdown = currentBeerlist.length + 1;
      // console.log(id_dropdown);

      let newBeer = {
        "id_history": id_history,
        "id_on_next": id_history,
        "id_dropdown": id_dropdown,
        "venue_db_id": ""
      }
      // console.log(newBeer);
      // Add new beer to list_current table in DB
      BeerCtrl.callFetchAddBeerToDB(newBeer);
      // use pusher to update UI on all screens with the new beer
      UpdateCtrl.callFetchAddUpdateScreenUI();
      e.preventDefault();
    }







    async function delBeerFromBeerlist(e) {
      console.log('CLICK MINUS BUTTON TO DELETE BEER FROM LISTS');

      let res = await UserCtrl.callFetchUserData();
      // console.log(res);
      let { id,  updated } = res;
      userId = id[0];
      // console.log(userId);
      // get the ID of the last beer in the beerlist to be removed from the DB
      // deletes last beer of the beerlist on the edit_beer_list UI
      let beer_id = UICtrl.callDeleteBeerFromListEditor(userId);
      // console.log(beer_id);
      // deletes the beer from the DB using the ID of the beer return deleting on the UI
      BeerCtrl.callFetchDeleteBeerFromDb(beer_id);

      UpdateCtrl.callFetchDeleteUpdateScreenUI();
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

  // Public methods
  return {
    init: function(){
      // loadUpdatePusher();
      // loadPusher();
      // addBeerToDbPusher();
      // editBeerToDbPusher();
      // delBeerFromDbPusher();
      // loadWinePusher();

      // Show flash message div and then hide after 2.5 seconds
      UICtrl.callHideFlashMsg();
      // BeerCtrl.callFetchCurrentBeerList(UICtrl.callUpdateDisplayScreen);
      // WineCtrl.callFetchCurrentWinelist(UICtrl.callUpdateWineTabletScreen);

      // Call load event listeners function
      loadEventListeners();
      // console.log("TRYING TO INITIALIZE THE SCREENS!!!!!!!!!")
      // initScreens({"updated":"True"});

    }
  }

})(UserCtrl, UpdateCtrl, BeerCtrl, WineCtrl, EventCtrl, ScreenSettingsCtrl, UICtrl);

// Initialize App
App.init();
