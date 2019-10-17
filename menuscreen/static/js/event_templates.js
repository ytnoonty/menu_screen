class EventTemplate {
  updateScreenSettings = (settings) => {

  }

  eventTwoColTemplate(data) {
    const { events, screenSettings, userSettings } = data;
    let eventsData = events;
    let screenSettingsData = screenSettings;
    let userSettingsData = userSettings;
    console.log("EVENT 2 COLUMN TEMPLATE");
    console.log("EVENT 2 COLUMN TEMPLATE");
    console.log("EVENT 2 COLUMN TEMPLATE");
    console.log("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%");
    console.log(data);

    let screenDisplay;
    let screenElementUserId = 'user-id-' + userSettingsData.venue_db_id;


    let displayElement = document.querySelector('#' + screenElementUserId);
    if (displayElement !== null) {
      displayElement = document.querySelector('#' +  screenElementUserId + ' #screen-display');
    }
    let displayElementHTML = '';
    let displayElementTicker = document.querySelector('.ticker');
    let displayElementTickerHTML = '';
    
    eventsData.forEach(event => {
      console.log(event.artist);
      displayElementHTML = `
        <div>${event.name}</div>
      `;

    });

    if (displayElement !== null && displayElement !== undefined) {
      displayElement.innerHTML = displayElementHTML;
      displayElementTicker.innerHTML = displayElementTickerHTML;
    }
    console.log("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%");
    console.log("EVENT 2 COLUMN TEMPLATE");
    console.log("EVENT 2 COLUMN TEMPLATE");
    console.log("EVENT 2 COLUMN TEMPLATE");
    console.log("EVENT 2 COLUMN TEMPLATE");
  }

}
