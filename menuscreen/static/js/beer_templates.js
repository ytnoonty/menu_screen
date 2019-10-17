class BeerTemplate {
  constructor() {
    this.updateScreenTemplates = (settings) => {
      console.log("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^");
      console.log("BEER TEMPLATE CONSTRUCTOR")
      console.log("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^");

      let beerNames = document.querySelectorAll('.beer-name');
      let beerStyles = document.querySelectorAll('.beer-style');
      let beerAbvs = document.querySelectorAll('.beer-abv');
      let beerBrewerys = document.querySelectorAll('.beer-brewery');
      let backgrounds = document.querySelectorAll('.background');
      let data = {
        "beerName": beerNames,
        "beerStyles": beerStyles,
        "beerAbvs": beerAbvs,
        "beerBrewerys": beerBrewerys,
        "backgrounds": backgrounds,
      }
      console.log(data);
      console.log(settings);
      beerNames.forEach(name => {
        name.style.fontSize = `${settings.nameFontSizeHTML}`;
        name.style.color = `${settings.nameFontColor}`;
      });
      // beerStyles.forEach(style => {
      //   style.style.fontSize = `${settings.styleFontSizeHTML}`;
      //   style.style.color = `${settings.styleFontColor}`;
      // });
      beerAbvs.forEach(abv => {
        abv.style.fontSize = `${settings.abvFontSizeHTML}`;
        abv.style.color = `${settings.abvFontColor}`;
      });
      beerBrewerys.forEach(brewery => {
        brewery.style.fontSize = `${settings.breweryFontSizeHTML}`;
        brewery.style.color = `${settings.breweryFontColor}`;
      });
      backgrounds.forEach(background => {
        background.style.backgroundImage = `linear-gradient(${settings.backgroundColorDirection}, ${settings.backgroundColorOne}, ${settings.backgroundColorTwo}, ${settings.backgroundColorThree})`;
      });

    }
  }

  addBeerOnTapNextDisplayTemplate(data) {
    console.log("/////////////////////////////////////////////////////////");
    console.log("CLICK THE PLUS SIGN ADD BEER TO ON TAP NEXT DISPLAY");
    console.log("addBeerOnTapNextDisplayTemplate");
    console.log("/////////////////////////////////////////////////////////");
    console.log(data);
    const { currentBeers, nextBeers, beerslistTotal, userSettings } = data;
    let beerlistOnTapNext = beerslistTotal.beerlist;
    console.log(nextBeers);

    let userIdData = userSettings.venue_db_id;

    let screenElementUserId = 'user-id-' + userIdData;
    console.log(screenElementUserId);
    let screenDisplay;
    let displayElement = document.querySelector('#' + screenElementUserId);
    console.log(displayElement);
    if (displayElement != null) {
      console.log("IN THE DISPLAY");
      console.log(displayElement);
      screenDisplay = document.querySelector('#' + screenElementUserId + ' #on-tap-next-display')
      if (screenDisplay != null) {
        console.log(screenDisplay);
      }
    }

    let screenDisplayHTML = ``;
    screenDisplayHTML += `
      <div class="row">
        <div class="col-12">
          <table id="on-tap-next-display-table" class="beerlist beers table table-striped">
            <tr>
              <th></th>
              <th>Currently on Tap</th>
              <th></th>
              <th>On Tap Next</th>
            </tr>
    `;
    currentBeers.forEach((beer, i, arr) => {
      screenDisplayHTML += `<tr class="beer">
        <td> ${ i+1 }. </td>
        <td><div class="currentBeer"> ${ arr[i].name } ${ arr[i].brewery } </div></td>
        <td><i class="arrow"></i></td>
        <td class="nextBeer"> ${ nextBeers[i].name } </td>
      </tr>`;
    });
    screenDisplayHTML += `
          </table>
        </div>
      </div>
    `;
    if (screenDisplay != null) {
      screenDisplay.innerHTML = screenDisplayHTML;
    }
  }

  addBeerOnTapNextEditorTemplate(data) {
    console.log("{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}");
    console.log("CLICK THE PLUS SIGN ADD BEER TO ON TAP NEXT EDITOR");
    console.log("addBeerOnTapNextEditorTemplate");
    console.log("{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}");
    console.log(data);
    const { currentBeers, nextBeers, beerslistTotal, userSettings } = data;
    let beerlistTot = beerslistTotal.beerlist;
    console.log(nextBeers);

    let userIdData = userSettings.venue_db_id;

    let screenElementUserId = `user-id-` + userIdData;
    console.log(screenElementUserId);
    let screenDisplay;
    let displayElement = document.querySelector('#' + screenElementUserId);
    console.log(displayElement);
    if (displayElement != null) {
      console.log("IN THE DISPLAY");
      console.log(displayElement);
      screenDisplay = document.querySelector('#' + screenElementUserId + ' #on-tap-next-editor-table');
      if (screenDisplay != null) {
        console.log(screenDisplay);
      }
    }

    let screenDisplayHTML = ``;
    let x = "";
    // <table id="on-tap-next-editor-table" class="beerlist beers table table-striped">
    screenDisplayHTML += `
        <tr>
          <th></th>
          <th>On Tap Now</th>
          <td><div></div></td>
          <th>Next to Tap</th>
        </tr>
    `;
    currentBeers.forEach((beer, index) => {
      x = index++;
      console.log(x);
      screenDisplayHTML += `
        <tr class="beer">
          <td>${ index }</td>
          <td><div class="currentBeer">${ beer.name } ${ beer.brewery }</div></td>
          <td><i class="arrow"></i></td>
          <td>
            <div class="form-group">
              <select id="beer_${ index }" class="form-control" name="beer_${ index }">
              `;
              beerlistTot.forEach((totBeer) => {
                if (totBeer.id == nextBeers[x].id_on_next) {
                  // console.log(`IN THE IF: id_dropdown: ${totBeer.id_dropdown} ${totBeer.id} totBeer: ${totBeer.name} nextBeers: ${nextBeers[index].id_on_next}`);
                  screenDisplayHTML += `
                    <option value="${ totBeer.id }" selected>${ totBeer.name }</option>
                  `;
                } else {
                  // console.log(`IN THE IFELSE: id_dropdown: ${totBeer.id_dropdown} ${totBeer.id} totBeer: ${totBeer.name} nextBeers: ${nextBeers[index].id_on_next}`);
                  screenDisplayHTML += `
                    <option value="${ totBeer.id }">${ totBeer.name}</option>
                  `;
                }
              });
      screenDisplayHTML += `
              </select>
            </div>
          </td>
        </tr>
      `;
    });

    // screenDisplayHTML += `
    //   </table>
    //   <div class="row d-flex justify-content-between">
    //     <div class="col-4">
    //       <input id="edit-on-tap-next-editor-submit" class="btn btn-sm btn-outline-primary" type="click" value="Submit">
    //     </div>
    //   </div>
    // </div>
    // `;

    if (screenDisplay != null) {
      screenDisplay.innerHTML = ``;
      screenDisplay.innerHTML = screenDisplayHTML;
    }
  }



  addBeerToListEditorTemplate(data) {
    // edit_beer_list add beer to the beerlist
      console.log("/////////////////////////////////////////////////////////////////");
      console.log("/////////////////////////////////////////////////////////////////");
      console.log("/////////////////////////////////////////////////////////////////");
      console.log('CLICK THE PLUS SIGN TO ADD BEER TO LIST');
      // console.log(data);
      console.log("/////////////////////////////////////////////////////////////////");
      console.log("/////////////////////////////////////////////////////////////////");
      console.log("/////////////////////////////////////////////////////////////////");
      // let { beerlist, venue_db_id } = data;
      let { currentBeers, nextBeers, beerslistTotal, userSettings } = data;
      // console.log(currentBeers);
      // console.log(nextBeers);
      // console.log(beerslistTotal);
      // console.log(userSettings);
      let beerlistData = beerslistTotal.beerlist;
      let userIdData = userSettings.venue_db_id;
      // console.log(beerlistData);
      // console.log(userIdData);

      let userId;
      console.log(document.querySelector('.user-id-edit-beerlist'));
      if (document.querySelector('.user-id-edit-beerlist') !== null) {
        userId = document.querySelector('.user-id-edit-beerlist').id.split('-')[2];
      } else {
        console.log(document.querySelector('.user-id-edit-beerlist'));
        // userId = document.querySelector('.user-id-edit-beerlist').id.split('-')[2];
        // console.log(userId);
      }
      // console.log(userId);

      if (userId == userIdData) {
        console.log("TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE");
        console.log("TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE");
        console.log("TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE");
        let screenElementUserId = 'user-id-' + userIdData;
        // console.log(screenElementUserId);

        let screenDisplay;
        let displayElement = document.querySelector('#' + screenElementUserId);
        // console.log(displayElement);
        if (displayElement != null) {
          // console.log("IN THE DISPLAY ELEMENT");
          // console.log(displayElement);
          displayElement = document.querySelector('#' + screenElementUserId + ' #beerlist');
          // console.log(displayElement);
          screenDisplay = displayElement;
          // console.log(screenDisplay);
        }

        const beerlistForm = document.querySelector('#edit-beerlist-form');
        const beerlistId = document.querySelector('#beerlist');
        const beers = document.querySelectorAll('.beers');
        let beersLen = beers.length;

        var beerContainerDivNode = document.createElement("div");
        var opsContainerDivNode = document.createElement("div");

        var selectDivNode = document.createElement("div");;
        var selectLabelNode = document.createElement("label");
        var selectNode = document.createElement("select");
        var option = document.createElement("option");

        var bomDivNode = document.createElement("div");;
        var bomCheckLabelNode = document.createElement("label");
        var bomCheckbox = document.createElement("input");

        var comingSoonDivNode = document.createElement("div");;
        var comingSoonCheckLabelNode = document.createElement("label");
        var comingSoonCheckbox = document.createElement("input");
        var breakNode = document.createElement("br");
        var hrEl = document.createElement("hr");

        beerContainerDivNode.classList = "beers";

        selectDivNode.classList = "form-group";
        selectNode.classlist = "form-contol, beer";
        selectNode.id = `beer_${beersLen + 1}`;
        selectLabelNode.innerHTML = `Beer ${beersLen + 1}`;
        selectLabelNode.htmlFor = selectNode.id;
        selectNode.classList = "form-control beer";
        selectNode.name = `beer_${beersLen + 1}`;

        for (let i = 0; i < beerlistData.length; i++) {
            // console.log(beerlistData[i]);
            option.value = beerlistData[i].id;
            option.text = beerlistData[i].name;
            selectNode.options[i] = new Option(beerlistData[i].name, i);
            selectNode.options[i].value = beerlistData[i].id;
            // console.log(selectNode.innerHTML);
        }

        // edit_beer_list add beer of the month checkbox
        bomDivNode.classList.add("form-group");
        bomCheckbox.id = `bom-beer_${beersLen + 1}`;
        bomCheckbox.setAttribute("type", "checkbox");
        bomCheckbox.setAttribute("name", `beer-of-month_${beersLen + 1}`);
        bomCheckbox.setAttribute("value", `1`);
        var spanBomTextNode = document.createElement("span");
        spanBomTextNode.innerHTML = " Beer of the month";
        bomCheckLabelNode.htmlFor = bomCheckbox.id;
        bomDivNode.appendChild(bomCheckLabelNode);
        bomDivNode.appendChild(bomCheckbox);
        bomDivNode.appendChild(spanBomTextNode);
        bomDivNode.appendChild(breakNode);

        // edit_beer_list add coming soon checkbox
        comingSoonDivNode.classList.add("form-group");
        comingSoonDivNode.classList.add("pl-5");
        comingSoonCheckbox.id = `comingSoon-beer_${beersLen + 1}`;
        comingSoonCheckbox.setAttribute("type", "checkbox");
        comingSoonCheckbox.setAttribute("name", `coming-soon_${beersLen + 1}`);
        comingSoonCheckbox.setAttribute("value", `1`);
        var spanBomTextNode = document.createElement("span");
        spanBomTextNode.innerHTML = " Coming soon";
        comingSoonCheckLabelNode.htmlFor = comingSoonCheckbox.id;
        comingSoonDivNode.appendChild(comingSoonCheckLabelNode);
        comingSoonDivNode.appendChild(comingSoonCheckbox);
        comingSoonDivNode.appendChild(spanBomTextNode);
        comingSoonDivNode.appendChild(breakNode);

        opsContainerDivNode.classList = "ops-container d-flex flex-row";
        opsContainerDivNode.appendChild(bomDivNode);
        opsContainerDivNode.appendChild(comingSoonDivNode);

        selectDivNode.appendChild(selectLabelNode);
        selectDivNode.appendChild(selectNode);

        beerContainerDivNode.appendChild(selectDivNode);
        beerContainerDivNode.appendChild(opsContainerDivNode);
        beerContainerDivNode.appendChild(hrEl);

        // beers[beersLen-1].parentElement.insertAdjacentElement("beforeend", beerContainerDivNode);
        if (screenDisplay != null) {
          screenDisplay.insertAdjacentElement("beforeend", beerContainerDivNode);
          }
      } else {
        console.log("FALSE FALSE FALSE FALSE FALSE");
        console.log("FALSE FALSE FALSE FALSE FALSE");
        console.log("FALSE FALSE FALSE FALSE FALSE");
        console.log("FALSE FALSE FALSE FALSE FALSE");
        console.log("FALSE FALSE FALSE FALSE FALSE");
      }
  }


  // delete last beer from the beerlist editor when the minus sign button is clicked
  deleteBeerFromListEditorTemplate(data) {
    // console.log(data);
    let displayElement;
    let screenElementUserId = 'user-id-' + data;
    displayElement = document.querySelector('#' + screenElementUserId);
    if (displayElement != null) {
      // console.log(displayElement);
      displayElement = document.querySelector('#' + screenElementUserId + ' #beerlist');
      // console.log(displayElement);
    }
    //edit_beer_list remove the beer from the list
    let beers = document.querySelectorAll('.beers');
    // get count of beers in list
    let beersLen = beers.length;
    // if only one beer left in list won't beer deleted
    if (beersLen > 1){
      //remove last beer in the list
      displayElement.lastElementChild.remove();
    }
    // return last beer of the list's number to be used for DB manipulation
    // i.e. delete the beer from the list in the DB
    return beersLen;
  }
  // delete last beer from beerlist for the on_tap_next_display
  deleteBeerFromOnTapNextDisplayTemplate(data) {
    console.log("DELETE FROM ON TAP NEXT DISPLAY");
    console.log(data);
    let displayElement;
    let screenElementUserId = 'user-id-' + data;
    displayElement = document.querySelector('#' + screenElementUserId);
    console.log(displayElement);
    if (displayElement != null) {
      displayElement = document.querySelector('#' + screenElementUserId + ' #on-tap-next-display-table');
        if (displayElement != null) {
        console.log(displayElement);
        let beers = document.querySelectorAll('.beer');
        console.log(beers);
        let beersLen = beers.length;
        console.log(beersLen);
        if (beersLen > 1) {
          displayElement.lastElementChild.lastElementChild.remove();
        }
      }
    }
  }
  // delete last beer from beerlist for the on_tap_next_display
  deleteBeerFromOnTapNextEditorTemplate(data) {
    console.log("DELETE FROM ON TAP NEXT EDITOR");
    console.log(data);
    let displayElement;
    let screenElementUserId = 'user-id-' + data;
    displayElement = document.querySelector('#' + screenElementUserId);
    console.log(displayElement);
    if (displayElement != null) {
      displayElement = document.querySelector('#' + screenElementUserId + ' #on-tap-next-editor-table');
      if (displayElement != null) {
        console.log(displayElement);
        let beers = document.querySelectorAll('.beer');
        console.log(beers);
        let beersLen = beers.length;
        console.log(beersLen);
        if (beersLen > 1) {
          displayElement.lastElementChild.lastElementChild.remove();
        }
      }
    }
  }






  // displays 2 columns of cards, each card has name on top line and style, abv, ibu on bottome line
  defaultTemplate(displayData) {
    console.log("**************************************************************************");
    console.log("IN THE DEFAULT TEMPLATE");
    console.log("**************************************************************************");
    console.log(displayData);
    const { currentBeers, events, screenSettings, userSettings } = displayData;
    let beersData = currentBeers;
    let eventsData = events;
    let screenSettingsData = screenSettings;
    let userSettingsData = userSettings;
    console.log(beersData);
    console.log(eventsData);
    console.log(screenSettingsData);
    console.log(userSettingsData);

    let beerlist = [];
    let beerlistBom = [];
    let beerlistCs = [];

    beersData.forEach(function(beer){
      if (!beer.beer_of_month && !beer.coming_soon ) {
        beerlist.push(beer);
      } else if (beer.beer_of_month && beer.coming_soon) {
        beerlistBom.push(beer);
        beerlistCs.push(beer);
      } else if (beer.beer_of_month){
        beerlist.push(beer);
        beerlistBom.push(beer);
      } else if (beer.coming_soon) {
        beerlistCs.push(beer);
      }
    });


    let halflistNum;
    halflistNum = Math.floor(beerlist.length / 2);

    let beerlistFirstHalf = beerlist.slice(0,halflistNum);
    let beerlistSecondHalf = beerlist.slice(halflistNum, beerlist.length);

    let screenDisplay;
    // console.log(userSettingsData.venue_db_id);
    let screenElementUserId = 'user-id-' + userSettingsData.venue_db_id;
    // console.log(screenElementUserId);

    let displayElement = document.querySelector('#' + screenElementUserId);
    if (displayElement != null) {
      // console.log(displayElement);
      displayElement = document.querySelector('#' + screenElementUserId + ' #screen-display');
      // console.log(displayElement);
      screenDisplay = displayElement;
      // console.log(screenDisplay);
    }

    let screenDisplayHTML = '';
    let screenDisplayTicker = document.querySelector('.ticker');
    let screenDisplayTickerHTML = '';
    screenDisplayHTML = `
    <div class="row mt-3">
      <div class="col-lg">
        <div class="list-group">
          <ul class="list-group-flush list-group-bts">`;
            beerlistFirstHalf.forEach(function(beer){
              screenDisplayHTML += `
              <li class="cardvs background">
                <table>
                  <tr>
                    <h1 class="italic-font bold-font txt-clr-ylw left-spacer no-btm-margin"><span class="beer-name">${beer.name}</span></h1>
                  </tr>
                  <tr class="left-spacer beer-screen-tr font-sml">
                    <td class="bold-font w-third"><span class="beer-style">${beer.style}</span></td>
                    <td class="w-fifth"><span class="font-xxsml"></span><span class="beer-abv">${beer.abv}</span><span class="font-xsml">%</span></td>
                    <td class="italic-font bold-font w-third"><span class="beer-brewery">${beer.brewery}</span></td>
                  </tr>
                </table>
              </li>`
            });
    screenDisplayHTML += `
          </ul>
        </div>
      </div>
      <div class="col-lg">
        <div class="list-group">
          <ul class="list-group-flush list-group-bts">`;
            beerlistSecondHalf.forEach(function(beer){
              screenDisplayHTML += `
              <li class="cardvs background">
                <table>
                  <tr>
                    <h1 class="italic-font bold-font txt-clr-ylw left-spacer no-btm-margin"><span class="beer-name">${beer.name}</span></h1>
                  </tr>
                  <tr class="left-spacer beer-screen-tr font-sml">
                    <td class="bold-font w-third"><span class="beer-style">${beer.style}</span></td>
                    <td class="w-fifth"><span class="font-xxsml"></span><span class="beer-abv">${beer.abv}</span><span class="font-xsml">%</span></td>
                    <td class="italic-font bold-font w-third"><span class="beer-brewery">${beer.brewery}</span></td>
                  </tr>
                </table>
              </li>`
            });
    screenDisplayHTML += `
          </ul>
        </div>
      </div>
    </div>`;

    screenDisplayTickerHTML = `

    `;
    screenDisplayTickerHTML = `
      <ul class="list-bts-coming-soon bold-font">
        <li class="info beer-month txt-clr-grn-shdw spacing-sml">Beer 'O the Month:</li>`;

        beerlistBom.forEach(function(beer){
          screenDisplayTickerHTML += `<li class="info info1 card-img txt-clr-ylw beerOfMonth beer-name">${beer.name}</li>`
        });

        screenDisplayTickerHTML += `
          <li class="info tap-soon txt-clr-grn-shdw spacing-sml">Tapping Soon:</li>
        `;

        beerlistCs.forEach(function(beer){
          screenDisplayTickerHTML += `<li class="info info2 card-img-before txt-clr-ylw beer-name">${beer.name}</li>`
        });

        screenDisplayTickerHTML += `
          <li class="info shams-news txt-clr-grn-shdw spacing-sml">Shamrock News:</li>
        `;

        screenDisplayTickerHTML += `
          <li class="info info6 card-img-after txt-clr-ylw beer-name"> SHAMROCK NEWS GOES HERE  </li>
      </ul>
    `;
    if (screenDisplay !== null && screenDisplay !== undefined) {
      screenDisplay.innerHTML = screenDisplayHTML;
      screenDisplayTicker.innerHTML = screenDisplayTickerHTML;
      this.updateScreenTemplates(screenSettingsData);
    }
  }

  // displays 2 columns of cards, each card with name on top line and style and ABV and IBU on bottom line of card
  twoColNSAITemplate(displayData){
    const { beers, events, screenSettings, userSettings } = displayData;
    let beersData = beers;
    let eventsData = events;
    let userSettingsData = userSettings;
    // console.log(beersData);
    // console.log(eventsData);
    // console.log(userSettingsData);

    let data0116 = beersData.slice(0,16);
    let data1722 = beersData.slice(16,22);
    let data0108 = beersData.slice(0,8);
    let data0816 = beersData.slice(8,16);

    // let screenDisplay = document.getElementById('screen-display');
    let screenDisplay;

    console.log(userSettingsData.venue_db_id);
    let screenElementUserId = 'user-id-' + userSettingsData.venue_db_id;
    console.log(screenElementUserId);

    let displayElement = document.querySelector('#' + screenElementUserId);
    if (displayElement != null) {
      console.log(displayElement);
      displayElement = document.querySelector('#' + screenElementUserId + ' #screen-display');
      console.log(displayElement);
      screenDisplay = displayElement;
      console.log(screenDisplay);
    }

    let screenDisplayHTML = '';
    let screenDisplayTicker = document.querySelector('.ticker');
    let screenDisplayTickerHTML = '';
    screenDisplayHTML = `
    <div class="row mt-3">
      <div class="col-lg">
        <div class="list-group">
          <ul class="list-group-flush list-group-bts">`;
            data0108.forEach(function(beer){
              screenDisplayHTML += `
              <li class="cardvs background">
                <table>
                  <tr>
                    <h1 class="italic-font bold-font txt-clr-ylw left-spacer no-btm-margin"><span class="beer-name">${beer.name}</span></h1>
                  </tr>
                  <tr class="left-spacer beer-screen-tr font-sml">
                    <td class="bold-font w-third"><span class="beer-style">${beer.style}</span></td>
                    <td class="w-fifth"><span class="font-xxsml"></span><span class="beer-abv">${beer.abv}</span><span class="font-xsml">%</span></td>
                  </tr>
                </table>
              </li>`
            });
    screenDisplayHTML += `
          </ul>
        </div>
      </div>
      <div class="col-lg">
        <div class="list-group">
          <ul class="list-group-flush list-group-bts">`;
            data0816.forEach(function(beer){
              screenDisplayHTML += `
              <li class="cardvs background">
                <table>
                  <tr>
                    <h1 class="italic-font bold-font txt-clr-ylw left-spacer no-btm-margin"><span class="beer-name">${beer.name}</span></h1>
                  </tr>
                  <tr class="left-spacer beer-screen-tr font-sml">
                    <td class="bold-font w-third"><span class="beer-style">${beer.style}</span></td>
                    <td class="w-fifth"><span class="font-xxsml"></span><span class="beer-abv">${beer.abv}</span><span class="font-xsml">%</span></td>
                  </tr>
                </table>
              </li>`
            });
    screenDisplayHTML += `
          </ul>
        </div>
      </div>
    </div>`;
    console.log('***************************************************************************************');
    console.log(data1722);
    console.log('***************************************************************************************');
    screenDisplayTickerHTML = `
      <ul class="list-bts-coming-soon bold-font">
        <li class="info beer-month txt-clr-grn-shdw spacing-sml">Beer 'O the Month:</li>
        <li class="info info1 card-img txt-clr-ylw beerOfMonth beer-name">${data1722[0].name}</li>
        <li class="info tap-soon txt-clr-grn-shdw spacing-sml">Tapping Soon:</li>
        <li class="info info2 card-img-before txt-clr-ylw beer-name">${data1722[1].name}</li>
        <li class="info info3 card-img-before txt-clr-ylw beer-name">${data1722[2].name}</li>
        <li class="info info4 card-img-before txt-clr-ylw beer-name">${data1722[3].name}</li>
        <li class="info info5 card-img txt-clr-ylw beer-name">${data1722[4].name}$</li>
        <li class="info shams-news txt-clr-grn-shdw spacing-sml">Shamrock News:</li>
        <li class="info info6 card-img-after txt-clr-ylw beer-name">${data1722[5].description}</li>
      </ul>
    `;
    if (screenDisplay !== null) {
      screenDisplay.innerHTML = screenDisplayHTML;
      screenDisplayTicker.innerHTML = screenDisplayTickerHTML;
      this.updateScreenTemplates(screenSettings);
    }
  }
  // displays 2 columns of cards, each card with name on top line and style and ABV on bottom line of card
  twoColNSTemplate(displayData){
    const { beers, events, screenSettings, userSettings } = displayData;
    let beersData = beers;
    let eventsData = events;
    let userSettingsData = userSettings;
    // console.log(beersData);
    // console.log(eventsData);
    // console.log(userSettingsData);

    let data0116 = beersData.slice(0,16);
    let data1722 = beersData.slice(16,22);
    let data0108 = beersData.slice(0,8);
    let data0816 = beersData.slice(8,16);

    // let screenDisplay = document.getElementById('screen-display');
    let screenDisplay;

    // console.log(userSettingsData.venue_db_id);
    let screenElementUserId = 'user-id-' + userSettingsData.venue_db_id;
    // console.log(screenElementUserId);

    let displayElement = document.querySelector('#' + screenElementUserId);
    if (displayElement != null) {
      // console.log(displayElement);
      displayElement = document.querySelector('#' + screenElementUserId + ' #screen-display');
      // console.log(displayElement);
      screenDisplay = displayElement;
      // console.log(screenDisplay);
    }

    let screenDisplayHTML = '';
    let screenDisplayTicker = document.querySelector('.ticker');
    let screenDisplayTickerHTML = '';
    screenDisplayHTML = `
    <div class="row mt-3">
      <div class="col-lg">
        <div class="list-group">
          <ul class="list-group-flush list-group-bts">`;
            data0108.forEach(function(beer){
              screenDisplayHTML += `
              <li class="cardvs background">
                <table>
                  <tr>
                    <h1 class="italic-font bold-font txt-clr-ylw left-spacer no-btm-margin"><span class="beer-name">${beer.name}</span></h1>
                  </tr>
                  <tr class="left-spacer beer-screen-tr font-sml">
                    <td class="bold-font w-third"><span class="beer-style">${beer.style}</span></td>
                  </tr>
                </table>
              </li>`
            });
    screenDisplayHTML += `
          </ul>
        </div>
      </div>
      <div class="col-lg">
        <div class="list-group">
          <ul class="list-group-flush list-group-bts">`;
            data0816.forEach(function(beer){
              screenDisplayHTML += `
              <li class="cardvs background">
                <table>
                  <tr>
                    <h1 class="italic-font bold-font txt-clr-ylw left-spacer no-btm-margin"><span class="beer-name">${beer.name}</span></h1>
                  </tr>
                  <tr class="left-spacer beer-screen-tr font-sml">
                    <td class="bold-font w-third"><span class="beer-style">${beer.style}</span></td>
                  </tr>
                </table>
              </li>`
            });
    screenDisplayHTML += `
          </ul>
        </div>
      </div>
    </div>`;
    // console.log('***************************************************************************************');
    // console.log(data1722);
    // console.log('***************************************************************************************');
    screenDisplayTickerHTML = `
      <ul class="list-bts-coming-soon bold-font">
        <li class="info beer-month txt-clr-grn-shdw spacing-sml">Beer 'O the Month:</li>
        <li class="info info1 card-img txt-clr-ylw beerOfMonth beer-name">${data1722[0].name}</li>
        <li class="info tap-soon txt-clr-grn-shdw spacing-sml">Tapping Soon:</li>
        <li class="info info2 card-img-before txt-clr-ylw beer-name">${data1722[1].name}</li>
        <li class="info info3 card-img-before txt-clr-ylw beer-name">${data1722[2].name}</li>
        <li class="info info4 card-img-before txt-clr-ylw beer-name">${data1722[3].name}</li>
        <li class="info info5 card-img txt-clr-ylw beer-name">${data1722[4].name}$</li>
        <li class="info shams-news txt-clr-grn-shdw spacing-sml">Shamrock News:</li>
        <li class="info info6 card-img-after txt-clr-ylw beer-name">${data1722[5].description}</li>
      </ul>
    `;
    if (screenDisplay !== null && screenDisplay !== undefined) {
      screenDisplay.innerHTML = screenDisplayHTML;
      screenDisplayTicker.innerHTML = screenDisplayTickerHTML;
      this.updateScreenTemplates(screenSettings);
    }
  }

  draftBeersPrintScreenTemplate(displayData){
    const { currentBeers, events, userSettings } = displayData;
    let beersData = currentBeers;
    // console.log(beersData);
    let userSettingsData = userSettings;
    // console.log(userSettingsData);

    let beerlist = [];
    let beerlistBom = [];
    let beerlistCs = [];

    beersData.forEach(function(beer){
      if (!beer.beer_of_month && !beer.coming_soon ) {
        beerlist.push(beer);
      } else if (beer.beer_of_month && beer.coming_soon) {
        beerlistBom.push(beer);
        beerlistCs.push(beer);
      } else if (beer.beer_of_month){
        beerlist.push(beer);
        beerlistBom.push(beer);
      } else if (beer.coming_soon) {
        beerlistCs.push(beer);
      }
    });

    let halflistNum;
    halflistNum = Math.floor(beerlist.length / 2);
    let beerlistFirstHalf = beerlist.slice(0,halflistNum);
    let beerlistSecondHalf = beerlist.slice(halflistNum, beerlist.length);

    let beersPrintScreenDiv = document.querySelector('.beer-list-div-bp');
    // console.log(userSettingsData.venue_db_id);
    let screenElementUserId = 'user-id-' + userSettingsData.venue_db_id;
    // console.log(screenElementUserId);
    let displayListElement = document.querySelector('#' + screenElementUserId);
    // console.log(displayListElement);
    displayListElement = document.querySelector('#' + screenElementUserId + ' .beer-list-div-bp');
    // console.log(displayListElement);
    beersPrintScreenDiv = displayListElement;
    // console.log(beersPrintScreenDiv);

    let beersPrintHTML = '';
    beersPrintHTML += `<ul id="" class='list-group-flush'>`;
    beerlist.forEach(function(beer){
      beersPrintHTML += `<li id="" class='list-group-item'>${beer.id_dropdown}.  <span class="larger-text txt-clr-grn">${beer.name}</span> - ${beer.style} - ${beer.abv}% ABV - ${beer.ibu} IBU - ${beer.location} - <span class="italic-font">${beer.brewery}</span></li>`;
    });
    beersPrintHTML += `</ul>`;

    if (beersPrintScreenDiv !== null) {
      // console.log(beersPrintScreenDiv);
      beersPrintScreenDiv.innerHTML = beersPrintHTML;
    }

    let monthPBPHTML = '';
    beerlistBom.forEach(function(beer){
      monthPBPHTML += `<span class="mx-3 larger-text txt-clr-grn">${beer.name}</span>`;
    });

    let monthPBP = document.querySelectorAll('.month-p-bp');
    let displayMonthElement = document.querySelector('#' + screenElementUserId + ' .month-p-bp');
    monthPBP = displayMonthElement;
    if (monthPBP !== null) {
      monthPBP.innerHTML = monthPBPHTML;
    }

    let comingsoonHTML = '';
    let comingsoonPBP = document.querySelector('#comingsoon-p-bp');
    let displayComingsoonElement = document.querySelector('#' + screenElementUserId + ' #comingsoon-p-bp');
    comingsoonPBP = displayComingsoonElement;
    beerlistCs.forEach(function(beer){
      // console.log(beer);
      comingsoonHTML += `<span class="mx-4 larger-text txt-clr-grn">${beer.name}</span>`;
    });
    if (comingsoonPBP !== null) {
      comingsoonPBP.innerHTML = comingsoonHTML;
    }
  }

  draftBeersTabletScreenTemplate(displayData){
    console.log("/////////////////////////////////////////////////////////////");
    console.log("draftBeersTabletScreenTemplate");
    console.log("/////////////////////////////////////////////////////////////");
    const { currentBeers, events, userSettings } = displayData;
    let beersData = currentBeers;
    // console.log(beersData);
    let userSettingsData = userSettings;
    // console.log(userSettingsData);

    let beerlist = [];
    let beerlistBom = [];
    let beerlistCs = [];

    beersData.forEach(function(beer){
      if (!beer.beer_of_month && !beer.coming_soon ) {
        beerlist.push(beer);
      } else if (beer.beer_of_month && beer.coming_soon) {
        beerlistBom.push(beer);
        beerlistCs.push(beer);
      } else if (beer.beer_of_month){
        beerlist.push(beer);
        beerlistBom.push(beer);
      } else if (beer.coming_soon) {
        beerlistCs.push(beer);
      }
    });

    let halflistNum;
    halflistNum = Math.floor(beerlist.length / 2);
    let beerlistFirstHalf = beerlist.slice(0,halflistNum);
    let beerlistSecondHalf = beerlist.slice(halflistNum, beerlist.length);

    let beersTabletScreenDivPP = document.querySelector('.beer-list-div-pp');
    // console.log(userSettingsData.venue_db_id);
    let screenElementUserId = 'user-id-' + userSettingsData.venue_db_id;
    // console.log(screenElementUserId);
    let displayListElement = document.querySelector('#' + screenElementUserId);
    // console.log(displayListElement);
    displayListElement = document.querySelector('#' + screenElementUserId + ' .beer-list-div-pp');
    // console.log(displayListElement);
    beersTabletScreenDivPP = displayListElement;
    // console.log(beersTabletScreenDivPP);

    let beersTabletHTML = '';
        beersTabletHTML += `<ul id="" class='beer-list-loop-pp list-group-flush'>`;
    beerlist.forEach(function(beer){
      beersTabletHTML += `<li id="" class='list-group-item-pp list-group-item'>${beer.id_dropdown}.  <span class="larger-text txt-clr-grn">${beer.name}</span> - <span class="bold-font italic-font">${beer.style}</span> - ${beer.abv}% ABV - ${beer.ibu} IBU - ${beer.location} - <span class="italic-font">${beer.brewery}</span></li>`;
    });
    beersTabletHTML += `</ul>`;

    if (beersTabletScreenDivPP !== null) {
      // console.log(beersTabletScreenDivPP);
      beersTabletScreenDivPP.innerHTML = beersTabletHTML;
    }

    let monthPPPHTML = '';
    beerlistBom.forEach(function(beer){
      monthPPPHTML += `
        <span class="mx-3 larger-text txt-clr-grn">${beer.name}</span> - <span class="bold-font italic-font">${beer.style}</span>
        `;
    });

    let monthPPP = document.querySelectorAll('.month-p-pp');
    let displayMonthElement = document.querySelector('#' + screenElementUserId + ' .month-p-pp');
    monthPPP = displayMonthElement;
    if (monthPPP !== null) {
      monthPPP.innerHTML = monthPPPHTML;
    }

    let comingsoonHTML = '';
    let comingsoonPPP = document.querySelector('#comingsoon-p-pp');
    let displayComingsoonElement = document.querySelector('#' + screenElementUserId + ' #comingsoon-p-pp');
    comingsoonPPP = displayComingsoonElement;
    beerlistCs.forEach(function(beer){
      comingsoonHTML += `<span class="mx-4 larger-text txt-clr-grn">${beer.name}</span>`;
    });
    if (comingsoonPPP !== null) {
      comingsoonPPP.innerHTML = comingsoonHTML;
    }
  }

  bottleBeersTabletScreenTemplate(displayData){
    console.log(displayData);
    const { beerslistTotal, userSettings } = displayData;
    let beersData = beerslistTotal.beerlist;
    console.log(beersData);
    let userId = userSettings.venue_db_id;
    console.log(userId);

    let screenElementUserId = 'user-id-' + userId;
    console.log(screenElementUserId);
    let displayListElement = document.querySelector('#' + screenElementUserId + ' .beer-list-loop-bb');
    if (displayListElement != null) {
      console.log(displayListElement);

      let bottleBeerlistHTML = "";
      bottleBeerlistHTML += `<ul id="bottle-beers-list" class="beer-list-loop-bb list-group-flush">`;
      beersData.forEach(beer=> {
        // if (beer.draft_bottle_selection == "Bottle" || beer.draft_bottle_selection == "Can" || beer.draft_bottle_selection == "Draft & Bottle" || beer.draft_bottle_selection == "Draft & Can" || beer.draft_bottle_selection == "Bottle & Can" || beer.draft_bottle_selection == "Draft, Bottle & Can") {
        if (beer.draft_bottle_selection != "Draft") {
          bottleBeerlistHTML += `<li class="list-group-item-bb list-group-item"><span class="larger-text txt-clr-grn">${beer.name} </span> ${beer.draft_bottle_selection} - <span class="bold-font italic-font">${beer.style}</span> - ${beer.abv}% ABV - ${beer.ibu} IBU - ${beer.location} - <span class="italic-font">${beer.brewery}</span></li>`;
        }
      });
      bottleBeerlistHTML += `</ul>`;
      displayListElement.innerHTML = bottleBeerlistHTML;
    }
  }

}
