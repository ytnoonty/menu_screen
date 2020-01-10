class BeerTemplate {
  constructor() {
    this.updateScreenTemplates = (settings) => {
      console.log("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^");
      console.log("BEER TEMPLATE CONSTRUCTOR")
      console.log("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^");

      let beerNames = document.querySelectorAll('.beer-name');
      let beerStyles = document.querySelectorAll('.beer-style');
      let beerAbvs = document.querySelectorAll('.beer-abv');
      let beerIbus = document.querySelectorAll('.beer-ibu');
      let beerBrewerys = document.querySelectorAll('.beer-brewery');
      let backgrounds = document.querySelectorAll('.background');
      let bomBackgrounds = document.querySelectorAll('.bom-background');
      let tickerWrapper = document.querySelector('.ticker-wrapper');
      let tickerText = document.querySelectorAll('.ticker-text');
      let tickerNews = document.querySelectorAll('.ticker-news');
      let data = {
        "beerName": beerNames,
        "beerStyles": beerStyles,
        "beerAbvs": beerAbvs,
        "beerBrewerys": beerBrewerys,
        "backgrounds": backgrounds,
        "tickerText": tickerText,
        "tickerNews": tickerNews,
      }
      // console.log(data);
      console.log(settings);
      beerNames.forEach(name => {
        name.style.color = `${settings.beerNameFontColor}`;
        name.style.fontFamily = `${settings.beerNameFont}`;
        name.style.fontSize = `${settings.beerNameFontSizeDisplay}`;
        if (settings.beerNameFontBoldToggle == true) {
          console.log(settings.beerNameFontBoldToggle);
          name.style.fontStyle = "bold";
        } else {
          name.style.fontStyle = "normal";
        }
        if (settings.beerNameFontItalicToggle == true) {
          console.log(settings.beerNameFontItalicToggle);
          name.style.fontStyle = "italic";
        } else {
          name.style.fontStyle = "normal";
        }
        if (settings.beerNameFontUnderlineToggle == true) {
          console.log(settings.beerNameFontUnderlineToggle);
          name.style.borderBottom = `thin solid ${settings.beerNameFontColor}`;
        } else {
          name.style.borderBottom = "none";
        }
      });


      beerStyles.forEach(style => {
        style.style.color = `${settings.beerStyleFontColor}`;
        style.style.fontSize = `${settings.beerStyleFontSizeDisplay}`;
      });

      beerAbvs.forEach(abv => {
        abv.style.color = `${settings.beerAbvFontColor}`;
        abv.style.fontSize = `${settings.beerAbvFontSizeDisplay}`;
      });

      beerIbus.forEach(ibu => {
        ibu.style.color = `${settings.beerIbuFontColor}`;
        ibu.style.fontSize = `${settings.beerIbuFontSizeDisplay}`;
      });

      beerBrewerys.forEach(brewery => {
        brewery.style.color = `${settings.beerBreweryFontColor}`;
        brewery.style.fontSize = `${settings.beerBreweryFontSizeDisplay}`;
      });

      backgrounds.forEach(background => {
        background.style.backgroundImage = `linear-gradient(${settings.beerBgColorDirection}, ${settings.beerBgColorOne}, ${settings.beerBgColorTwo}, ${settings.beerBgColorThree}, ${settings.beerBgColorFour}, ${settings.beerBgColorFive})`;
      });

      bomBackgrounds.forEach(background => {
        background.style.backgroundImage = `linear-gradient(${settings.beerBomBgColorDirection}, ${settings.beerBomBgColorOne}, ${settings.beerBomBgColorTwo},${settings.beerBomBgColorThree}, ${settings.beerBomBgColorFour}, ${settings.beerBomBgColorFive})`;
      });

      tickerText.forEach(text => {
        text.style.color = `${settings.beerTickerFontColor}`;
        text.style.fontSize = `${settings.beerTickerFontSizeDisplay}`;
      });
      tickerNews.forEach(news => {
        news.style.color = `${settings.beerTickerFontColor}`;
        news.style.fontSize = `${settings.beerTickerFontSizeDisplay}`;
      });

      tickerWrapper.style.backgroundImage = `linear-gradient(${settings.beerTickerBgColorDirection}, ${settings.beerTickerBgColorOne}, ${settings.beerTickerBgColorTwo},${settings.beerTickerBgColorThree}, ${settings.beerTickerBgColorFour}, ${settings.beerTickerBgColorFive})`;

      (function(Ticker, settings, tickerWrapper){
        const ticker = Ticker();
        ticker.callLoadTicker(settings, tickerWrapper);
        ticker.callMoveTicker(settings);

      })(Ticker, settings, tickerWrapper);

      // ability to change screen orientation
      // example code to update screen orientaion, update "element" with correct screen element
      // Using CSS
      // transform: rotate(90deg);
      // Using js
      // element.style.transform = 'rotate(90deg)';
      const rotater = Rotater();
      rotater.callRotateScreen(settings);


    } //END updateScreenTemplates

    const Rotater = () => {
      function logRotater(settingsData) {
        console.log(settingsData.beerscreenLandscapePortraitToggle);
      }

      function rotateScreen(settingsData) {
        console.log(settingsData.beerscreenLandscapePortraitToggle);
        console.log(`settingsData.beerscreenLandscapePortraitToggle: ${settingsData.beerscreenLandscapePortraitToggle}`);

        if ( settingsData.beerscreenLandscapePortraitToggle == true ) {
          console.log(settingsData.screenDisplay.parentElement.parentElement.parentElement);
          let w = window.innerWidth;
          console.log(w);
          console.log(settingsData.screenDisplay.parentElement.parentElement.parentElement.clientWidth);
          let h = window.innerHeight;
          console.log(h);
          console.log(settingsData.screenDisplay.parentElement.parentElement.parentElement.clientHeight);
          // settingsData.screenDisplay.parentElement.parentElement.parentElement.style.transform = 'rotate(270deg)';
          // settingsData.screenDisplay.parentElement.parentElement.parentElement.style.width = `${ h }px`;
          // settingsData.screenDisplay.parentElement.parentElement.parentElement.style.height = `${ w }px`;
        } else {
          console.log(settingsData.screenDisplay.parentElement.parentElement.parentElement);
          let w = window.innerWidth;
          console.log(w);
          let h = window.innerHeight;
          console.log(h);
        //   settingsData.screenDisplay.parentElement.parentElement.parentElement.style.width = window.innerHeight;
        //   settingsData.screenDisplay.parentElement.parentElement.parentElement.style.height = window.innerWidth;
        //   settingsData.screenDisplay.parentElement.parentElement.parentElement.style.transform = 'rotate(0deg)';
        }
      }

      return {
        callLogRotater : (settingsData) => {
          logRotater(settingsData);
        },
        callRotateScreen : (settingsData) => {
          rotateScreen(settingsData);
        },
      }
    }


    const Ticker = () => {
      // Animation comes from animations.js
      const loadTicker = (settings, tickerWrapper) => {
        console.log('function loadTicker()');
        let tickerAnimation = Animation;

        if (settings.beerTickerToggle) {
          tickerWrapper.classList.remove('d-none');
        } else {
          tickerWrapper.classList.add('d-none');
        }
      } // end loadTicker

      const moveTicker = (settings) => {
        console.log('function moveTicker()');
        let ticker = document.querySelector('.ticker');
        let tickerItems = document.querySelector('.ticker-items');
        let tickerItem = document.querySelectorAll('.ticker-item');
        let tickerDuration;
        const tickerAnimation = new Animation();

        let liTotalWidth = 0;
        let tickerWidth = 0;
        let totalDivTicker = 0;
        let totalLiWidth = 0;
        tickerItem.forEach(item => {
          let elWidth = tickerAnimation.getElementWidth(item);
          let beforePseudoWidth = tickerAnimation.getPseudoElementWidth(item, "before", "width");
          let afterPseudoWidth = tickerAnimation.getPseudoElementWidth(item, "after", "width");
          totalLiWidth += elWidth + beforePseudoWidth + afterPseudoWidth;
        });
        // console.log(totalLiWidth);
        let widthMovement = "translateX(-" + totalLiWidth + "px)";
        // console.log(widthMovement);
        // console.log(settings.beerTickerScrollSpeed);
        if (settings.beerTickerScrollSpeed !== null || settings.beerTickerScrollSpeed !== '') {
          tickerDuration = totalLiWidth * settings.beerTickerScrollSpeed;
        } else {
          tickerDuration = totalLiWidth * 10;
        }
        // console.log(tickerDuration);
        // console.log(tickerItems);
        tickerAnimation.animateTicker(tickerItems, widthMovement, tickerDuration);
      } // end moveTicker

      return {
        callLoadTicker: (x, y) => {
          loadTicker(x, y);
        },
        callMoveTicker: (x) => {
          moveTicker(x);
        },
      }
    } // END FUNCITON TICKER
  } // END CONSTRUCTOR

  addBeerOnTapNextDisplayTemplate(data) {
    // console.log("/////////////////////////////////////////////////////////");
    // console.log("CLICK THE PLUS SIGN ADD BEER TO ON TAP NEXT DISPLAY");
    // console.log("addBeerOnTapNextDisplayTemplate");
    // console.log("/////////////////////////////////////////////////////////");
    // console.log(data);
    const { currentBeers, nextBeers, beerslistTotal, userSettings } = data;
    let beerlistOnTapNext = beerslistTotal.beerlist;
    // console.log(nextBeers);

    let userIdData = userSettings.venue_db_id;
    // console.log(userIdData);

    if (Object.getOwnPropertyNames(userIdData).length >= 1) {

          let screenElementUserId = 'user-id-' + userIdData;
          // console.log(screenElementUserId);
          let screenDisplay;
          let displayElement = document.querySelector('#' + screenElementUserId);
          // console.log(displayElement);
          if (displayElement != null) {
            // console.log("IN THE DISPLAY");
            // console.log(displayElement);
            screenDisplay = document.querySelector('#' + screenElementUserId + ' #on-tap-next-display')
            if (screenDisplay != null) {
              // console.log(screenDisplay);
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
  }

  addBeerOnTapNextEditorTemplate(data) {
    // console.log("{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}");
    // console.log("CLICK THE PLUS SIGN ADD BEER TO ON TAP NEXT EDITOR");
    // console.log("addBeerOnTapNextEditorTemplate");
    // console.log("{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}");
    // console.log(data);
    const { currentBeers, nextBeers, beerslistTotal, userSettings } = data;
    let beerlistTot = beerslistTotal.beerlist;
    // console.log(nextBeers);

    let userIdData = userSettings.venue_db_id;

    if (Object.getOwnPropertyNames(userIdData).length >= 1) {

          let screenElementUserId = `user-id-` + userIdData;
          // console.log(screenElementUserId);
          let screenDisplay;
          let displayElement = document.querySelector('#' + screenElementUserId);
          // console.log(displayElement);
          if (displayElement != null) {
            // console.log("IN THE DISPLAY");
            // console.log(displayElement);
            screenDisplay = document.querySelector('#' + screenElementUserId + ' #on-tap-next-editor-table');
            if (screenDisplay != null) {
              // console.log(screenDisplay);
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
            // console.log(x);
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
  }



  addBeerToListEditorTemplate(data) {
    // edit_beer_list add beer to the beerlist
      console.log("/////////////////////////////////////////////////////////////////");
      console.log("/////////////////////////////////////////////////////////////////");
      console.log("/////////////////////////////////////////////////////////////////");
      console.log('CLICK THE PLUS SIGN TO ADD BEER TO LIST');
      console.log(data);
      console.log("/////////////////////////////////////////////////////////////////");
      console.log("/////////////////////////////////////////////////////////////////");
      console.log("/////////////////////////////////////////////////////////////////");
      // let { beerlist, venue_db_id } = data;
      let { currentBeers, nextBeers, beerslistTotal, userSettings } = data;
      console.log(currentBeers);
      // console.log(nextBeers);
      // console.log(beerslistTotal);
      // console.log(userSettings);
      let beerlistData = beerslistTotal.beerlist;
      let userIdData = userSettings.venue_db_id;
      // console.log(beerlistData);
      // console.log(userIdData);

      let userId;
      // console.log(document.querySelector('.user-id-edit-beerlist'));
      if (document.querySelector('.user-id-edit-beerlist') !== null) {
        userId = document.querySelector('.user-id-edit-beerlist').id.split('-')[2];
      } else {
        // console.log(document.querySelector('.user-id-edit-beerlist'));
        // userId = document.querySelector('.user-id-edit-beerlist').id.split('-')[2];
        // console.log(userId);
      }
      // console.log(userId);

      if (userId == userIdData) {
        console.log("TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE");
        // console.log("TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE");
        // console.log("TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE");
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
        // console.log("FALSE FALSE FALSE FALSE FALSE");
        // console.log("FALSE FALSE FALSE FALSE FALSE");
        // console.log("FALSE FALSE FALSE FALSE FALSE");
        // console.log("FALSE FALSE FALSE FALSE FALSE");
      }
  }

  repaintBeerListEditorTemplate(data) {
                            // edit_beer_list add beer to the beerlist
                              // console.log("/////////////////////////////////////////////////////////////////");
                              // console.log("/////////////////////////////////////////////////////////////////");
                              // console.log("/////////////////////////////////////////////////////////////////");
                              console.log('CHANGED TO A DIFFERENT SCREEN FROM EDIT BEERLIST SCREEN');
                              // console.log(data);
                              // console.log("/////////////////////////////////////////////////////////////////");
                              // console.log("/////////////////////////////////////////////////////////////////");
                              // console.log("/////////////////////////////////////////////////////////////////");
                              // let { beerlist, venue_db_id } = data;
                              let { currentBeers, nextBeers, beerslistTotal, tickerInfo, userSettings } = data;
                              // console.log(currentBeers);
                              // console.log(tickerInfo);
                              // console.log(nextBeers);
                              // console.log(beerslistTotal);
                              // console.log(userSettings);
                              let beerlistData = beerslistTotal.beerlist;
                              let userIdData = userSettings.venue_db_id;
                              // console.log(beerlistData);
                              // console.log(userIdData);

                              let userId;
                              // console.log(document.querySelector('.user-id-edit-beerlist'));
                              if (document.querySelector('.user-id-edit-beerlist') !== null) {
                                userId = document.querySelector('.user-id-edit-beerlist').id.split('-')[2];
                              } else {
                                // console.log(document.querySelector('.user-id-edit-beerlist'));
                                // userId = document.querySelector('.user-id-edit-beerlist').id.split('-')[2];
                                // console.log(userId);
                              }
                              // console.log(userId);
      if (userId == userIdData) {
          console.log("TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE");
          // console.log("TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE");
          // console.log("TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE");
          let screenElementUserId = 'user-id-' + userIdData;
          // console.log(screenElementUserId);

          let screenDisplay;
          let displayElement = document.querySelector('#' + screenElementUserId);
          // console.log(displayElement);
          if (displayElement != null) {
            console.log("IN THE DISPLAY ELEMENT");
            // console.log(displayElement);
            displayElement = document.querySelector('#' + screenElementUserId + ' #beerlist');
            // console.log(displayElement);
            screenDisplay = displayElement;
            // console.log(screenDisplay);
          }

            let tickerTextEl = document.querySelector('#ticker-text');
            screenDisplay.innerHTML = '';
            currentBeers.forEach(beer => {
              // console.log("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
              // console.log("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
              // console.log(beer);
              // console.log(beer.id_history);
              // console.log(beer.id_dropdown);
              // console.log("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
              // console.log("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
                      //
                      // div with .beers
                      var beerContainerDivNode = document.createElement("div");
                      beerContainerDivNode.classList = "beers";

                      // select node
                      var selectLabelNode = document.createElement("label");
                      var selectDivNode = document.createElement("div");;
                      var selectNode = document.createElement("select");
                      var option = document.createElement("option");

                      // div for beer of month and coming soon
                      var opsContainerDivNode = document.createElement("div");

                      var bomDivNode = document.createElement("div");;
                      var bomCheckLabelNode = document.createElement("label");
                      var bomCheckbox = document.createElement("input");

                      var comingSoonDivNode = document.createElement("div");;
                      var comingSoonCheckLabelNode = document.createElement("label");
                      var comingSoonCheckbox = document.createElement("input");

                      var breakNode = document.createElement("br");
                      var hrEl = document.createElement("hr");

                      selectDivNode.classList = "form-group";
                      selectNode.classList = `form-control edit-beer edit-beer-${beer.id_dropdown}`;

                      selectNode.id = `beer_${beer.id_dropdown}`;
                      selectLabelNode.innerHTML = `Beer ${beer.id_dropdown}`;
                      selectLabelNode.htmlFor = selectNode.id;
                      selectNode.name = `beer_${beer.id_dropdown}`;

                      for (let i = 0; i < beerlistData.length; i++) {
                          // console.log(i, beer.id_history, beerlistData[i].id[0], beerlistData[i]);
                          option.value = beerlistData[i].id;
                          option.text = beerlistData[i].name;
                          selectNode.options[i] = new Option(beerlistData[i].name, i);
                          selectNode.options[i].value = beerlistData[i].id;
                          // console.log(selectNode.innerHTML);
                          if (beer.id_history == beerlistData[i].id[0]) {
                            selectNode.options[i].selected = true;
                          }
                      }

                      // edit_beer_list add beer of the month checkbox
                      bomDivNode.classList.add("form-group");
                      // have to put a marginLeft in to compensate for textNode created when page is rendered
                      bomDivNode.style.marginLeft = "4px";
                      bomCheckbox.id = `bom-beer_${beer.id_dropdown}`;
                      bomCheckbox.setAttribute("type", "checkbox");
                      bomCheckbox.setAttribute("name", `beer-of-month_${beer.id_dropdown}`);
                      bomCheckbox.setAttribute("value", beer.beer_of_month);
                      bomCheckbox.checked = beer.beer_of_month;
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
                      // have to put a marginLeft in to compensate for textNode created when page is rendered
                      comingSoonDivNode.style.marginLeft = "4px";
                      comingSoonCheckbox.id = `comingSoon-beer_${beer.id_dropdown}`;
                      comingSoonCheckbox.setAttribute("type", "checkbox");
                      comingSoonCheckbox.setAttribute("name", `coming-soon_${beer.id_dropdown}`);
                      comingSoonCheckbox.setAttribute("value", beer.coming_soon);
                      comingSoonCheckbox.checked = beer.coming_soon;
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

                      // // beers[beersLen-1].parentElement.insertAdjacentElement("beforeend", beerContainerDivNode);
                      if (screenDisplay != null) {
                        screenDisplay.insertAdjacentElement("beforeend", beerContainerDivNode);
                      }

            });  // end forEach for currentBeerlist Select

            tickerTextEl.value = tickerInfo.ticker_text;

    } else {
      console.log("FALSE FALSE FALSE FALSE FALSE");
    }
  } // END repaintBeerListEditorTemplate
  //////////////////////////////////


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
    // // return last beer of the list's number to be used for DB manipulation
    // // i.e. delete the beer from the list in the DB
    // return beersLen;
  }
  // delete last beer from beerlist for the on_tap_next_display
  deleteBeerFromOnTapNextDisplayTemplate(data) {
    console.log("DELETE FROM ON TAP NEXT DISPLAY");
    // console.log(data);
    let displayElement;
    let screenElementUserId = 'user-id-' + data;
    displayElement = document.querySelector('#' + screenElementUserId);
    // console.log(displayElement);
    if (displayElement != null) {
      displayElement = document.querySelector('#' + screenElementUserId + ' #on-tap-next-display-table');
        if (displayElement != null) {
        // console.log(displayElement);
        let beers = document.querySelectorAll('.beer');
        // console.log(beers);
        let beersLen = beers.length;
        // console.log(beersLen);
        if (beersLen > 1) {
          displayElement.lastElementChild.lastElementChild.remove();
        }
      }
    }
  }
  // delete last beer from beerlist for the on_tap_next_display
  deleteBeerFromOnTapNextEditorTemplate(data) {
    console.log("DELETE FROM ON TAP NEXT EDITOR");
    // console.log(data);
    let displayElement;
    let screenElementUserId = 'user-id-' + data;
    displayElement = document.querySelector('#' + screenElementUserId);
    // console.log(displayElement);
    if (displayElement != null) {
      displayElement = document.querySelector('#' + screenElementUserId + ' #on-tap-next-editor-table');
      if (displayElement != null) {
        // console.log(displayElement);
        let beers = document.querySelectorAll('.beer');
        // console.log(beers);
        let beersLen = beers.length;
        // console.log(beersLen);
        if (beersLen > 1) {
          displayElement.lastElementChild.lastElementChild.remove();
        }
      }
    }
  }

  ////////////////////////////////////////////////////////////////////////////
  /////// BEGIN beer_dashboard
  ////////////////////////////////////////////////////////////////////////////
  repaintBeerDashboard(data) {
    let dashboardBeerInfo = document.querySelector('#dashboard-beer-info');
    let { beerlist } = data;
    // console.log(beerlist);
    // console.log("REPAINT BEER DASHBOARD LIST");
    let beerDashboardTable = document.createElement('table');
    beerDashboardTable.className = 'mt-3 table table-striped';
    beerlist.forEach(beer => {
      // console.log(beer);
      // get first letter of beer.name to put in tr id to be used by side menu for navigation of list
      let dashMenuId_firstLetter = beer.name[0].slice(0,1).toLowerCase();
      // console.log(dashMenuId_firstLetter);
      beerDashboardTable.innerHTML += `
      <tr id="${ dashMenuId_firstLetter }" class="row-name">
        <th class="toggle-table dashboard-beer-name">${beer.name}</th>
        <td><a href="edit_beer/${beer.id}" class="btn btn-sm btn-outline-default pull-right">Edit</a></td>
        <td>
          <form action="/delete_beer/${beer.id}" method="post">
            <input type="hidden" name="_method" value="DELETE">
            <input type="submit" value="Delete" class="btn btn-sm btn-outline-danger">
          </form>
        </td>
      </tr>
      <tr>
        <td colspan="2" class="d-none animate-table">
          <div class="row row-id">
            <div class="col-5">ID:</div>
            <div class="col-7">${beer.id}</div>
          </div>
          <div class="row row-style">
            <div class="col-5">Style:</div>
            <div class="col-7">${beer.style}</div>
          </div>
          <div class="row row-abv">
            <div class="col-5">ABV:</div>
            <div class="col-7">${beer.abv}</div>
          </div>
          <div class="row row-ibu">
            <div class="col-5">IBU:</div>
            <div class="col-7">${beer.ibu}</div>
          </div>
          <div class="row row-brewery">
            <div class="col-5">Brewery:</div>
            <div class="col-7">${beer.brewery}</div>
          </div>
          <div class="row row-location">
            <div class="col-5">Location:</div>
            <div class="col-7">${beer.location}</div>
          </div>
          <div class="row row-website">
            <div class="col-5">Website:</div>
            <div class="col-7">${beer.website}</div>
          </div>
          <div class="row row-description">
            <div class="col-5">Description:</div>
            <div class="col-7">${beer.description}</div>
          </div>
          <div class="row row-draft-bottle">
            <div class="col-5">Draft / Bottle:</div>
            <div class="col-7">${beer.draft_bottle_selection}</div>
          </div>
        </td>
      </tr>
      `;
    });
    dashboardBeerInfo.appendChild(beerDashboardTable);
  }
  ////////////////////////////////////////////////////////////////////////////
  /////// END beer_dashboard
  ////////////////////////////////////////////////////////////////////////////






  // displays 2 columns of cards, each card has name on top line and style, abv, ibu on bottome line
  defaultTemplate(displayData) {
    // console.log("**************************************************************************");
    // console.log("IN THE DEFAULT TEMPLATE");
    // console.log("**************************************************************************");
    // console.log(displayData);
    const { currentBeers, events, tickerInfo, screenSettings, userSettings } = displayData;
    let beersData = currentBeers;
    let eventsData = events;
    let tickerInfoData = tickerInfo;
    let screenSettingsData = screenSettings;
    let userSettingsData = userSettings;
    // console.log(beersData);
    // console.log(eventsData);
    // console.log(tickerInfoData);
    // console.log(screenSettingsData);
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
    }

    let screenDisplayHTML = '';
    let screenDisplayTicker = document.querySelector('.ticker-wrapper');
    let screenDisplayTickerHTML = '';
    screenDisplayHTML = `
    <div class="row mt-1">
      <div class="col-6 beerlist-col">
          <ul id="" class="list-group mx-2">`;


            beerlistFirstHalf.forEach(function(beer){

              if (!beer.beer_of_month) {
                screenDisplayHTML += `
                <li class="list-group-item card-beerscreen-display background">
                `;
              } else {
                screenDisplayHTML += `
                <li class="list-group-item card-beerscreen-display bom-background">
                `;
              }
              screenDisplayHTML += `
                <table class="beerscreen-display-table">
                  <tr class="">
                    <td class="font-weight-bold font-italic txt-clr-ylw pl-2 pt-1" colspan="3"><span class="beer-name">${beer.name}</span></td>
                  </tr>
                  <tr class="">
                    <td class="beerscreen-table-td-30 font-weight-bold pl-2"><span class="beer-style">${beer.style}</span></td>
                    <td class="beerscreen-table-td-20 font-weight-bold"><span class="font-xxsml"></span><span class="beer-abv">${beer.abv}</span><span class="">%</span></td>
                    <td class="beerscreen-table-td-50 font-weight-bold font-italic"><span class="beer-brewery">${beer.brewery}</span></td>
                  </tr>
                </table>
              </li>`
            });


    screenDisplayHTML += `
            </ul>
          </div>
        <div class="col-6 beerlist-col">
          <ul id="" class="list-group mr-2">`;
            beerlistSecondHalf.forEach(function(beer){

              if (!beer.beer_of_month) {
                screenDisplayHTML += `
                <li class="list-group-item card-beerscreen-display background">
                `;
              } else {
                screenDisplayHTML += `
                <li class="list-group-item card-beerscreen-display bom-background">
                `;
              }
              screenDisplayHTML += `
                <table class="beerscreen-display-table">
                  <tr class="">
                    <td class="font-weight-bold font-italic txt-clr-ylw pl-2 pt-1" colspan="3"><span class="beer-name">${beer.name}</span></td>
                  </tr>
                  <tr class="">
                    <td class="beerscreen-table-td-30 font-weight-bold pl-2"><span class="beer-style">${beer.style}</span></td>
                    <td class="beerscreen-table-td-20 font-weight-bold"><span class="font-xxsml"></span><span class="beer-abv">${beer.abv}</span><span class="">%</span></td>
                    <td class="beerscreen-table-td-50 font-weight-bold font-italic"><span class="beer-brewery">${beer.brewery}</span></td>
                  </tr>
                </table>
              </li>`
            });
    screenDisplayHTML += `
          </ul>
        </div>
      </div>`;

      screenDisplayTickerHTML = ``;
      screenDisplayTickerHTML = `
      <div class="ticker d-flex align-items-center move-left">
        <ul class="list-group ticker-items list-group-inline ml-3">
      `;
      if (beerlistBom.length > 0){
        screenDisplayTickerHTML += `
          <li class="list-group-inline align-middle font-weight-bold ticker-item txt-clr-grn-shdw spacing-sml"><span class="ticker-text">Beer 'O the Month:</span></li>
        `;
      }
      beerlistBom.forEach(function(beer){
        screenDisplayTickerHTML += `
          <li class="list-group-inline align-middle font-weight-bold font-italic ticker-item left-spacer txt-clr-ylw card-img"><span class="beer-name">${ beer.name }</span></li>
        `});
      if (beerlistCs.length > 0) {
        screenDisplayTickerHTML += `
          <li class="list-group-inline align-middle font-weight-bold ticker-item left-spacer txt-clr-grn-shdw spacing-sml"><span class="ticker-text">Tapping Soon:</span></li>
        `;
      }
      beerlistCs.forEach(function(beer){
        screenDisplayTickerHTML += `
          <li class="list-group-inline align-middle font-weight-bold font-italic ticker-item txt-clr-ylw card-img"><span class="beer-name">${ beer.name }</span></li>
      `});
      if (tickerInfoData.ticker_text !== "") {
        screenDisplayTickerHTML += `
          <li class="list-group-inline align-middle font-weight-bold ticker-item txt-clr-grn-shdw left-spacer spacing-sml"><span class="ticker-text">Shamrock News:</span></li>
          <li class="list-group-inline align-middle font-weight-bold font-italic ticker-item txt-clr-ylw left-spacer card-img"><span class="ticker-news">${ tickerInfoData.ticker_text }</span></li>
        `;
      }
        screenDisplayTickerHTML += `
        </ul>
      </div>
        `;

    if (screenDisplay !== null && screenDisplay !== undefined) {
      screenDisplay.innerHTML = screenDisplayHTML;
      screenDisplayTicker.innerHTML = screenDisplayTickerHTML;
      screenSettingsData.screenDisplay = screenDisplay;
      this.updateScreenTemplates(screenSettingsData);
    }
  }


  // displays 2 columns of cards, each card with name on top line and style and ABV and IBU on bottom line of card
  twoColNSAITemplate(displayData) {
    // console.log("**************************************************************************");
    // console.log("IN THE twoColNSAITemplate);
    // console.log("**************************************************************************");
    // console.log(displayData);
    const { currentBeers, events, tickerInfo, screenSettings, userSettings } = displayData;
    let beersData = currentBeers;
    let eventsData = events;
    let tickerInfoData = tickerInfo;
    let screenSettingsData = screenSettings;
    let userSettingsData = userSettings;
    // console.log(beersData);
    // console.log(eventsData);
    // console.log(tickerInfoData);
    // console.log(screenSettingsData);
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
    let screenDisplayTicker = document.querySelector('.ticker-wrapper');
    let screenDisplayTickerHTML = '';
    screenDisplayHTML = `
    <div class="row mt-1">
      <div class="col-6 beerlist-col">
          <ul id="" class="list-group mx-2">`;


            beerlistFirstHalf.forEach(function(beer){

              if (!beer.beer_of_month) {
                screenDisplayHTML += `
                <li class="list-group-item card-beerscreen-display background">
                `;
              } else {
                screenDisplayHTML += `
                <li class="list-group-item card-beerscreen-display bom-background">
                `;
              }
              screenDisplayHTML += `
                <table class="beerscreen-display-table">
                  <tr class="">
                    <td class="font-weight-bold font-italic txt-clr-ylw pl-2 pt-1" colspan="3"><span class="beer-name">${beer.name}</span></td>
                  </tr>
                  <tr class="">
                    <td class="beerscreen-table-td-30 font-weight-bold pl-2"><span class="beer-style">${beer.style}</span></td>
                    <td class="beerscreen-table-td-50 font-weight-bold"><span class="font-xxsml"></span><span class="beer-abv">${beer.abv}</span><span class="">%</span> - <span class="beer-ibu">${beer.ibu}</span> <span>IBU</span></td>

                  </tr>
                </table>
              </li>`
            });


    screenDisplayHTML += `
            </ul>
          </div>
        <div class="col-6 beerlist-col">
          <ul id="" class="list-group mr-2">`;
            beerlistSecondHalf.forEach(function(beer){

              if (!beer.beer_of_month) {
                screenDisplayHTML += `
                <li class="list-group-item card-beerscreen-display background">
                `;
              } else {
                screenDisplayHTML += `
                <li class="list-group-item card-beerscreen-display bom-background">
                `;
              }
              screenDisplayHTML += `
                <table class="beerscreen-display-table">
                  <tr class="">
                    <td class="font-weight-bold font-italic txt-clr-ylw pl-2 pt-1" colspan="3"><span class="beer-name">${beer.name}</span></td>
                  </tr>
                  <tr class="">
                    <td class="beerscreen-table-td-30 font-weight-bold pl-2"><span class="beer-style">${beer.style}</span></td>
                    <td class="beerscreen-table-td-50 font-weight-bold"><span class="font-xxsml"></span><span class="beer-abv">${beer.abv}</span><span class="">%</span> - <span class="beer-ibu">${beer.ibu}</span> <span>IBU</span></td>

                  </tr>
                </table>
              </li>`
            });
    screenDisplayHTML += `
          </ul>
        </div>
      </div>`;

      screenDisplayTickerHTML = ``;
      screenDisplayTickerHTML = `
      <div class="ticker d-flex align-items-center move-left">
        <ul class="list-group ticker-items list-group-inline ml-3">
      `;
      if (beerlistBom.length > 0){
        screenDisplayTickerHTML += `
          <li class="list-group-inline align-middle font-weight-bold ticker-item txt-clr-grn-shdw spacing-sml"><span class="ticker-text">Beer 'O the Month:</span></li>
        `;
      }
      beerlistBom.forEach(function(beer){
        screenDisplayTickerHTML += `
          <li class="list-group-inline align-middle font-weight-bold font-italic ticker-item left-spacer txt-clr-ylw card-img"><span class="beer-name">${ beer.name }</span></li>
        `});
      if (beerlistCs.length > 0) {
        screenDisplayTickerHTML += `
          <li class="list-group-inline align-middle font-weight-bold ticker-item left-spacer txt-clr-grn-shdw spacing-sml"><span class="ticker-text">Tapping Soon:</span></li>
        `;
      }
      beerlistCs.forEach(function(beer){
        screenDisplayTickerHTML += `
          <li class="list-group-inline align-middle font-weight-bold font-italic ticker-item txt-clr-ylw card-img"><span class="beer-name">${ beer.name }</span></li>
      `});
      if (tickerInfoData.ticker_text !== "") {
        screenDisplayTickerHTML += `
          <li class="list-group-inline align-middle font-weight-bold ticker-item txt-clr-grn-shdw left-spacer spacing-sml"><span class="ticker-text">Shamrock News:</span></li>
          <li class="list-group-inline align-middle font-weight-bold font-italic ticker-item txt-clr-ylw left-spacer card-img"><span class="ticker-news">${ tickerInfoData.ticker_text }</span></li>
        `;
      }
        screenDisplayTickerHTML += `
        </ul>
      </div>
        `;

    if (screenDisplay !== null && screenDisplay !== undefined) {
      screenDisplay.innerHTML = screenDisplayHTML;
      screenDisplayTicker.innerHTML = screenDisplayTickerHTML;
      this.updateScreenTemplates(screenSettingsData);
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


    if (Object.getOwnPropertyNames(beersData).length >= 1) {
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
                beersPrintHTML += `<li id="" class='list-group-item'>${beer.id_dropdown}.  <span class="larger-text txt-clr-grn">${beer.name}</span> - ${beer.style} - ${beer.abv}% ABV - ${beer.ibu} IBU - ${beer.location} - <span class="italic-font">${beer.brewery}</span></li><hr>`;
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
  }

  draftBeersTabletScreenTemplate(displayData){
    // console.log("/////////////////////////////////////////////////////////////");
    // console.log("draftBeersTabletScreenTemplate");
    // console.log("/////////////////////////////////////////////////////////////");
    const { currentBeers, events, userSettings } = displayData;
    let beersData = currentBeers;
    // console.log(beersData);
    let userSettingsData = userSettings;
    // console.log(userSettingsData);

    let beerlist = [];
    let beerlistBom = [];
    let beerlistCs = [];

    if (Object.getOwnPropertyNames(beersData).length >= 1) {

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
                beersTabletHTML += `<li id="" class='list-group-item-pp list-group-item'>${beer.id_dropdown}.  <span class="larger-text txt-clr-grn">${beer.name}</span> - <span class="bold-font italic-font">${beer.style}</span> - ${beer.abv}% ABV - ${beer.ibu} IBU - ${beer.location} - <span class="italic-font">${beer.brewery}</span></li><hr>`;
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
  }

  bottleBeersTabletScreenTemplate(displayData){
    console.log(displayData);
    const { bottleBeerlist, userSettings } = displayData;
    let beersData = bottleBeerlist.beerlist;
    console.log(beersData);

    let userId = userSettings.venue_db_id;
    // console.log(Object.getOwnPropertyNames(userId).length);

    // if (Object.getOwnPropertyNames(userId).length >= 1) {
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
    // }
  }

  paintUntappdSearchResultsList(displayData) {
    // console.log("IN THE BEER TEMPLATE paintUntappdSearchResultsList()");
    // console.log(displayData);
    const { beerData, userData } = displayData;
    // console.log(beerData);
    // console.log(userData);

    let userId = userData.id[0];
    let screenElementUserId = 'user-id-' + userId;
    // console.log(screenElementUserId);
    let displayListElement = document.querySelector('#' + screenElementUserId + ' #search-beer-results');
    if (displayListElement != null) {
      // console.log(displayListElement);
      let resultsHTML = "";

      resultsHTML = `
        <div class="accordion" id="beerlistAccordion"</div>
      `;
      beerData.forEach(beer => {
        resultsHTML += `
            <div class="card">
              <div class="card-header" id="heading-${beer.beer.bid}">
                <h2 class="mb-0">
                  <button class="btn btn-link" type="button" data-toggle="collapse" data-target="#${beer.beer.bid}" aria-expanded="false" aria-controls="${beer.beer.bid}">
                    <div>
                      <span class="beer-id">${beer.beer.bid}</span> - <span>${beer.beer.beer_name}</span><br><span>${beer.brewery.brewery_name}</span>
                    </div>
                  </button>
                  <div class="">
                    <a href="#heading-${beer.beer.bid}" class="btn btn-sm btn-outline-success untappd-add-beer-to-db" type="">Add Beer</a>
                  </div>
                </h2>
              </div>
              <div id="${beer.beer.bid}" class="collapse" aria-labelledby="heading-${beer.beer.bid}" data-parent="#beerlistAccordion">
                <div class="card-body">
                  <table class="table-striped">
                    <tr>
                      <th>Style - </th><td>${beer.beer.beer_style}</td>
                    </tr>
                    <tr>
                      <th>ABV - </th><td>${beer.beer.beer_abv}</td>
                    </tr>
                    <tr>
                      <th>IBU - </th><td>${beer.beer.beer_ibu}</td>
                    </tr>
                    <tr>
                      <th>Brewery - </th><td>${beer.brewery.brewery_name}</td>
                    </tr>
                    <tr>
                      <th>Location - </th><td>${beer.brewery.location.brewery_city}, ${beer.brewery.location.brewery_state}</td>
                    </tr>
                    <tr>
                      <th>Website - </th><td>${beer.brewery.contact.url}</td>
                    </tr>
                    <tr>
                      <th>Description - </th><td>${beer.beer.beer_description}</td>
                    </tr>
                    <tr>
                      <th></th>
                      <td>
                          <div>
                            <input class="bottle-draft-draft" type="radio" id="draft-${beer.beer.bid}"
                                   name="beer-${beer.beer.bid}" value="Draft" />
                            <label for="draft">Draft</label>
                          </div>
                          <div>
                            <input class="bottle-draft-bottle" type="radio" id="bottle-${beer.beer.bid}"
                                   name="beer-${beer.beer.bid}" value="Bottle" />
                            <label for="bottle">Bottle</label>
                          </div>
                          <div>
                            <input class="bottle-draft-can" type="radio" id="can-${beer.beer.bid}"
                                   name="beer-${beer.beer.bid}" value="Can" />
                            <label for="can">Can</label>
                          </div>
                          <div>
                            <input class="bottle-draft-draftBottle" type="radio" id="draftBottle-${beer.beer.bid}"
                                   name="beer-${beer.beer.bid}" value="Draft & Bottle" />
                            <label for="draftBottle">Draft & Bottle</label>
                          </div>
                          <div>
                            <input class="bottle-draft-draftCan" type="radio" id="draftCan-${beer.beer.bid}"
                                   name="beer-${beer.beer.bid}" value="Draft & Can" />
                            <label for="draftCan">Draft & Can</label>
                          </div>
                          <div>
                            <input class="bottle-draft-bottleCan" type="radio" id="bottleCan-${beer.beer.bid}"
                                   name="beer-${beer.beer.bid}" value="Bottle & Can" />
                            <label for="bottleCan">Bottle & Can</label>
                          </div>
                          <div>
                            <input class="bottle-draft-draftBottleCan" type="radio" id="draftBottleCan-${beer.beer.bid}"
                                   name="beer-${beer.beer.bid}" value="Draft, Bottle & Can" />
                            <label for="draftBottleCan">Draft, Bottle & Can</label>
                          </div>
                      </td>
                    </tr>
                  </table>
                </div>
              </div>
            </div>
        `;
      });
      resultsHTML += `
        </div>
      `;
      // console.log(resultsHTML);
      displayListElement.innerHTML = resultsHTML;
    }
    let draftRadios = document.querySelectorAll(".bottle-draft-draft");
    draftRadios.forEach(draftRadio => {
      // console.log(draftRadio);
      draftRadio.checked = true;
    });
  }

  repaintBeerscreenSettingsTemplate1(displayData) {
    console.log(displayData);
    const { screenSettings, fontSizeOptions } = displayData;
    // console.log(screenSettings);
    // console.log(fontSizeOptions);
    let beerscreenSettingsDiv = document.querySelector('#beerscreen_settings');
    let colorDirectionOptions = ["to bottom", "to top", "to left", "to right", "to bottom left", "to bottom right", "to top left", "to top right"];
    let fontOptions = ["","Courier New", "Times Roman"];
    // let fontSizeOptions = ["", "1.0em", "1.5em", "2.0em", "2.5em", "3.0em", "3.5em", "4.0em", "4.5em", "5.0em", "5.5em", "6.0em"];

    const colorOfEl = (settingsId, setting, labelTxt1, labelTxt2) => {
      let divHTML = ``;
      let divFormGroupWrapper = [`<div class="form-group">`, `</div>`];
      let divLabel = ``;
      let divBody = ``;
      divHTML += divFormGroupWrapper[0];
      divLabel = `
        <label for="${ settingsId }">${ labelTxt1 }</label>
        <input id="${ settingsId }" class="form-control" name="${ settingsId }" type="color" value="${ setting }">
      `;
      divHTML += divLabel;
      divBody = `
        <label for="${ settingsId }">${ labelTxt2 }</label>
        <input class="form-control" disabled="" id="${ settingsId }" name="${ settingsId }" type="text" value="${ setting }">
      `;
      divHTML += divBody;
      divHTML += divFormGroupWrapper[1];
      return divHTML;
    };

    const toggleSettingDiv = (settingsId, settings, labelTxt) => {
      let divHTML;
      let divFormGroupWrapper = [`<div class="form-group">`, `</div>`];
      let divLabel = `<label for="${ settingsId }">${ labelTxt }</label>`;
      let divBody = ``;
      if ( settings ) {
        divBody += `
          <input class="form-control" id="${ settingsId }" checked="" name="${ settingsId }" type="checkbox" value="y">
        `;
      } else {
        divBody += `
          <input class="form-control" id="${ settingsId }" name="${ settingsId }" type="checkbox" value="y">
        `;
      }
      divHTML = divFormGroupWrapper[0];
      divHTML += divLabel;
      divHTML += divBody;
      divHTML += divFormGroupWrapper[1];
      return divHTML;
    };

    const fontOptionsEl = (options, settingsId, settings, labelTxt) => {
      let divHTML;
      let divFormGroupWrapper = [`<div class="form-group">`, `</div>`];
      let divLabel=`
        <label for="${ settingsId }">${labelTxt}</label>
        <select class="form-control" id="${ settingsId }" name="${ settingsId }">
      `;
      let divBody;
      divHTML = divFormGroupWrapper[0];
      divHTML += divLabel;
      options.forEach((option, index) => {
        // console.log(index, option, settings, settingsId);
        if (index == settings) {
          divBody += `
            <option selected="" value="${ index }">${ option }</option>
          `;
        } else if (index > 0) {
          divBody += `
            <option value="${ index }">${ option }</option>
          `;
        } else {}
      });
      divHTML += divBody;
      divHTML += `
        </select>
      `;
      divHTML += divFormGroupWrapper[1];
      return divHTML;
    };

    const fontSizeOptionsEl = fontOptionsEl;

    const colorDirectionEl = (options, settingsId, settings, labelTxt) => {
      let divHTML;
      let divFormGroupWrapper = [`<div class="form-group">`, `</div>`];
      let divLabel = `
        <label for="${ settingsId }">${labelTxt}</label>
        <select class="form-control" id="${ settingsId }" name="${ settingsId }">
      `;
      let divBody;
      divHTML = divFormGroupWrapper[0];
      divHTML += divLabel;
      options.forEach(option => {
        if (option == settings) {
          divBody += `
            <option selected="" value="${ option }">${ option }</option>
          `;
        } else {
          divBody += `
            <option value="${ option }">${ option }</option>
          `;
        }
      });
      divHTML += divBody;
      divHTML += `
        </select>
      `;
      divHTML += divFormGroupWrapper[1];
      return divHTML;
    };

    // console.log(beerscreenSettingsDiv);
    // beerscreenTemplate select
    // clear the beerscreenSettings UI
    beerscreenSettingsDiv.innerHTML = ``;
    // build screen ID select
    let beerscreenIdSelectHTML = `
      <div class="row border border-secondary rounded mb-2">
        <div class="col-6">
          <div class="form-group">
            <label for="beerscreenTemplate">Screen Template:</label>
            <select id="beerscreenTemplate" class="form-control" name="beerscreenTemplate">
              <option selected="" value="1">2 Columns, Name, ABV, IBU</option>
            </select>
          </div>
        </div>
        <div class="col-12">
        `;
          beerscreenIdSelectHTML += toggleSettingDiv("beerscreenLandscapePortraitToggle", screenSettings.beerscreenLandscapePortraitToggle, "Portrait:");
          beerscreenIdSelectHTML += `
        </div>
      </div>
    `;
    beerscreenSettingsDiv.innerHTML += beerscreenIdSelectHTML;

    let fontColorsDivHTML = `
      <div class="row border border-secondary rounded mb-2">
        <div class="col-3">
        `;
          fontColorsDivHTML += colorOfEl("fontColorOne", screenSettings.fontColorOne, "Font Color #1:", "Font Color Code #1:");
          // fontColorsDivHTML += `
          //       <label for="fontColorOne">Font Color One:</label>
          //       <input id="fontColorOne" class="form-control" name="fontColorOne" type="color" value="${ screenSettings.fontColorOne }">
          //       <label for="fontColorOne">Font Color Code One:</label>
          //       <input class="form-control" disabled="" id="fontColorOne" name="fontColorOne" type="text" value="${ screenSettings.fontColorOne }">
          // `;
          fontColorsDivHTML += `
        </div>
        <div class="col-3">
        `;
          fontColorsDivHTML += colorOfEl("fontColorTwo", screenSettings.fontColorTwo, "Font Color #2:", "Font Color Code #2:");
          fontColorsDivHTML += `
        </div>
        <div class="col-3">
        `;
          fontColorsDivHTML += colorOfEl("fontColorThree", screenSettings.fontColorThree, "Font Color #3:", "Font Color Code #3:");
          fontColorsDivHTML += `
        </div>
        <div class="col-3">
        `;
          fontColorsDivHTML += colorDirectionEl(colorDirectionOptions, "fontColorDirection", screenSettings.fontColorDirection, "Font Color Direction:");
          fontColorsDivHTML += `
        </div>
      </div>
    `;

    beerscreenSettingsDiv.innerHTML += fontColorsDivHTML;

    let shadowFontColorHTML = `
      <div class="row border border-secondary rounded mb-2">
        <div class="col-3">
        `;
          shadowFontColorHTML +=  colorOfEl("shadowFontColorOne", screenSettings.shadowFontColorOne, "Shadow Color #1:", "Shadow Color Code #1:");
          shadowFontColorHTML += `
        </div>
        <div class="col-3">
        `;
          shadowFontColorHTML += colorOfEl("shadowFontColorTwo", screenSettings.shadowFontColorTwo, "Shadow Color #2:", "Shadow Color Code #2:");
          shadowFontColorHTML += `
        </div>
        <div class="col-3">
        `;
          shadowFontColorHTML += colorOfEl("shadowFontColorThree", screenSettings.shadowFontColorThree, "Shadow Color #3:", "Shadow Color Code #3:");
          shadowFontColorHTML += `
        </div>
        <div class="col-3">
        `;
          shadowFontColorHTML += colorDirectionEl(colorDirectionOptions, "shadowFontColorDirection", screenSettings.shadowFontColorDirection, "Shadow Color Direction:")
          shadowFontColorHTML += `
        </div>
      </div>
    `;
    beerscreenSettingsDiv.innerHTML += shadowFontColorHTML;

    let bomBgColorDivHTML = `
      <div class="row border border-secondary rounded mb-2">
        <div class="col-2">
        `;
          bomBgColorDivHTML += colorOfEl("beerBomBgColorOne", screenSettings.beerBomBgColorOne, "Beer of the Month Background Color #1:", "Beer of the Month Background Color Code #1:");
          bomBgColorDivHTML += `
        </div>
        <div class="col-2">
        `;
          bomBgColorDivHTML += colorOfEl("beerBomBgColorTwo", screenSettings.beerBomBgColorTwo, "Beer of the Month Background Color #2:", "Beer of the Month Background Color Code #2:");
          bomBgColorDivHTML += `
        </div>
        <div class="col-2">
        `;
          bomBgColorDivHTML += colorOfEl("beerBomBgColorThree", screenSettings.beerBomBgColorThree, "Beer of the Month Background Color #3:", "Beer of the Month Background Color Code #3:");
          bomBgColorDivHTML += `
        </div>
        <div class="col-2">
        `;
          bomBgColorDivHTML += colorOfEl("beerBomBgColorFour", screenSettings.beerBomBgColorFour, "Beer of the Month Background Color #4:", "Beer of the Month Background Color Code #4:");
          bomBgColorDivHTML += `
        </div>
        <div class="col-2">
        `;
          bomBgColorDivHTML += colorOfEl("beerBomBgColorFive", screenSettings.beerBomBgColorFive, "Beer of the Month Background Color #5:", "Beer of the Month Background Color Code #5:");
          bomBgColorDivHTML += `
        </div>
        <div class="col-2">
        `;
          bomBgColorDivHTML += colorDirectionEl(colorDirectionOptions, "beerBomBgColorDirection", screenSettings.beerBomBgColorDirection, "Beer of the Month Background Color Direction:");
          bomBgColorDivHTML += `
        </div>
      </div>
    `;
    beerscreenSettingsDiv.innerHTML += bomBgColorDivHTML;

    let bomNameSettingsDivHTML = `
      <div class="row border border-secondary rounded mb-2">
        <div class="col-2">
        `;
          bomNameSettingsDivHTML += fontOptionsEl(fontOptions, "beerBomNameFont",screenSettings.beerBomNameFont , "Beer of the Month Name Font:");
          bomNameSettingsDivHTML += `
        </div>
        <div class="col-2">
        `;
          bomNameSettingsDivHTML += colorOfEl("beerBomNameFontColor", screenSettings.beerBomNameFontColor, "Beer of the Month Name Font Color:", "Beer of the Month Name Font Color Code:");
          bomNameSettingsDivHTML += `
        </div>
        <div class="col-2">
        `;
          bomNameSettingsDivHTML += fontSizeOptionsEl(fontSizeOptions, "beerBomNameFontSize", screenSettings.beerBomNameFontSize, "Beer of the Month Name Font Size:");
          bomNameSettingsDivHTML += `
        </div>
        <div class="col-2">
        `;
          bomNameSettingsDivHTML += toggleSettingDiv("beerBomNameFontBoldToggle", screenSettings.beerBomNameFontBoldToggle, "Beer of the Month Name Bold:");
          // bomNameSettingsDivHTML += `
          //     <label for="beerBomNameFontBoldToggle">Beer of the Month Name Bold Font:</label>
          // `;
          //     if (screenSettings.beerBomNameFontBoldToggle) {
          //       bomNameSettingsDivHTML += `
          //         <input class="form-control" id="beerBomNameFontBoldToggle" checked="" name="beerBomNameFontBoldToggle" type="checkbox" value="y">
          //       `;
          //     } else {
          //       bomNameSettingsDivHTML += `
          //         <input class="form-control" id="beerBomNameFontBoldToggle" name="beerBomNameFontBoldToggle" type="checkbox" value="y">
          //       `;
          //     }
          bomNameSettingsDivHTML += `
        </div>
        <div class="col-2">
        `;
          bomNameSettingsDivHTML += toggleSettingDiv("beerBomNameFontItalicToggle", screenSettings.beerBomNameFontItalicToggle, "Beer of the Month Name Italic:");
          bomNameSettingsDivHTML += `
        </div>
        <div class="col-2">
        `;
          bomNameSettingsDivHTML += toggleSettingDiv("beerBomNameFontUnderlineToggle", screenSettings.beerBomNameFontUnderlineToggle, "Beer of the Month Name Underline:");
          bomNameSettingsDivHTML += `
        </div>
      </div>
    `;
    beerscreenSettingsDiv.innerHTML += bomNameSettingsDivHTML;

    let bomStyleSettingsDivHTML = `
        <div class="row border border-secondary rounded mb-2">
          <div class="col-2">
          `;
            bomStyleSettingsDivHTML += fontOptionsEl(fontOptions, "beerBomStyleFont", screenSettings.beerBomStyleFont, "Beer of the Month Style Font:");
            bomStyleSettingsDivHTML += `
          </div>
          <div class="col-2">
          `;
            bomStyleSettingsDivHTML += colorOfEl("beerBomStyleFontColor", screenSettings.beerBomStyleFontColor, "Beer of the Month Style Font Color:", "Beer of the Month Style Font Color Code:");
            bomStyleSettingsDivHTML += `
          </div>
          <div class="col-2">
          `;
            bomStyleSettingsDivHTML += fontSizeOptionsEl(fontSizeOptions, "beerBomStyleFontSize", screenSettings.beerBomStyleFontSize, "Beer of the Month Style Font Size:");
            bomStyleSettingsDivHTML += `
          </div>
          <div class="col-2">
          `;
            bomStyleSettingsDivHTML += toggleSettingDiv("beerBomStyleFontBoldToggle", screenSettings.beerBomStyleFontBoldToggle, "Beer of the Month Style Bold:");
            bomStyleSettingsDivHTML += `
          </div>
          <div class="col-2">
          `;
            bomStyleSettingsDivHTML += toggleSettingDiv("beerBomStyleFontItalicToggle", screenSettings.beerBomStyleFontItalicToggle, "Beer of the Month Style Italic:");
            bomStyleSettingsDivHTML += `
          </div>
          <div class="col-2">
          `;
            bomStyleSettingsDivHTML += toggleSettingDiv("beerBomStyleFontUnderlineToggle", screenSettings.beerBomStyleFontUnderlineToggle, "Beer of the Month Style Underline:");
            bomStyleSettingsDivHTML += `
          </div>
        </div>
    `;
    beerscreenSettingsDiv.innerHTML += bomStyleSettingsDivHTML;

    let bomAbvSettingsDivHTML = `
        <div class="row border border-secondary rounded mb-2">
          <div class="col-2">
            <div class="form-group">
            </div>
          </div>
          <div class="col-2">
          `;
            bomAbvSettingsDivHTML += colorOfEl("beerBomAbvFontColor", screenSettings.beerBomAbvFontColor, "Beer of the Month Abv Font Color:", "Beer of the Month Abv Font Color Code:");
            bomAbvSettingsDivHTML += `
          </div>
          <div class="col-2">
          `;
            bomAbvSettingsDivHTML += fontSizeOptionsEl(fontSizeOptions, "beerBomAbvFontSize", screenSettings.beerBomAbvFontSize, "Beer of the Month Abv Font Size:");
            bomAbvSettingsDivHTML += `
          </div>
          <div class="col-2">
          `;
            bomAbvSettingsDivHTML += toggleSettingDiv("beerBomAbvFontBoldToggle", screenSettings.beerBomAbvFontBoldToggle, "Beer of the Month Abv Bold:");
            bomAbvSettingsDivHTML += `
          </div>
          <div class="col-2">
          `;
            bomAbvSettingsDivHTML += toggleSettingDiv("beerBomAbvFontItalicToggle", screenSettings.beerBomAbvFontItalicToggle, "Beer of the Month Abv Italic:");
            bomAbvSettingsDivHTML += `
          </div>
          <div class="col-2">
          `;
            bomAbvSettingsDivHTML += toggleSettingDiv("beerBomAbvFontUnderlineToggle", screenSettings.beerBomAbvFontUnderlineToggle, "Beer of the Month Abv Underline:");
            bomAbvSettingsDivHTML += `
          </div>
        </div>
    `;
    beerscreenSettingsDiv.innerHTML += bomAbvSettingsDivHTML;

    let bomIbuSettingsDivHTML = `
        <div class="row border border-secondary rounded mb-2">
          <div class="col-2">
            <div class="form-group">
            </div>
          </div>
          <div class="col-2">
          `;
            bomIbuSettingsDivHTML += colorOfEl("beerBomIbuFontColor", screenSettings.beerBomIbuFontColor, "Beer of the Month Ibu Font Color:", "Beer of the Month Ibu Font Color Code:");
            bomIbuSettingsDivHTML += `
          </div>
          <div class="col-2">
          `;
            bomIbuSettingsDivHTML += fontSizeOptionsEl(fontSizeOptions,"beerBomIbuFontSize", screenSettings.beerBomIbuFontSize, "Beer of the Month Ibu Font Size:");
            bomIbuSettingsDivHTML += `
          </div>
          <div class="col-2">
          `;
            bomIbuSettingsDivHTML += toggleSettingDiv("beerBomIbuFontBoldToggle", screenSettings.beerBomIbuFontBoldToggle, "Beer of the Month Ibu Bold:");
            bomIbuSettingsDivHTML += `
          </div>
          <div class="col-2">
          `;
            bomIbuSettingsDivHTML += toggleSettingDiv("beerBomIbuFontItalicToggle", screenSettings.beerBomIbuFontItalicToggle, "Beer of the Month Ibu Italic:");
            bomIbuSettingsDivHTML += `
          </div>
          <div class="col-2">
          `;
            bomIbuSettingsDivHTML += toggleSettingDiv("beerBomIbuFontUnderlineToggle", screenSettings.beerBomIbuFontUnderlineToggle, "Beer of the Month Ibu Underline:");
            bomIbuSettingsDivHTML += `
          </div>
        </div>
    `;
    beerscreenSettingsDiv.innerHTML += bomIbuSettingsDivHTML;

    let bomBrewerySettingsDivHTML = `
        <div class="row border border-secondary rounded mb-2">
          <div class="col-2">
        `;
        bomBrewerySettingsDivHTML += fontOptionsEl(fontOptions, "beerBomBreweryFont", screenSettings.beerBomBreweryFont, "Beer of the Month Brewery Font");
        bomBrewerySettingsDivHTML += `
          </div>
          <div class="col-2">
            `;
        bomBrewerySettingsDivHTML +=  colorOfEl("beerBomBreweryFontColor", screenSettings.beerBomBreweryFontColor, "Beer of the Month Brewery Font Color:", "Beer of the Month Brewery Font Color Code:");
        bomBrewerySettingsDivHTML += `
          </div>
          <div class="col-2">
        `;
        bomBrewerySettingsDivHTML += fontSizeOptionsEl(fontSizeOptions,"beerBomBreweryFontSize", screenSettings.beerBomBreweryFontSize, "Beer of the Month Brewery Font Size:");
        bomBrewerySettingsDivHTML += `
          </div>
          <div class="col-2">
        `;
        bomBrewerySettingsDivHTML += toggleSettingDiv("beerBomBreweryFontBoldToggle", screenSettings.beerBomBreweryFontBoldToggle, "Beer of the Month Brewery Bold:");
        bomBrewerySettingsDivHTML += `
          </div>
          <div class="col-2">
        `;
        bomBrewerySettingsDivHTML += toggleSettingDiv("beerBomBreweryFontItalicToggle", screenSettings.beerBomBreweryFontItalicToggle, "Beer of the Month Brewery Italic:");
        bomBrewerySettingsDivHTML += `
          </div>
          <div class="col-2">
        `;
        bomBrewerySettingsDivHTML += toggleSettingDiv("beerBomBreweryFontUnderlineToggle", screenSettings.beerBomBreweryFontUnderlineToggle, "Beer of the Month Brewery Underline:");
        bomBrewerySettingsDivHTML += `
          </div>
        </div>
    `;
    beerscreenSettingsDiv.innerHTML += bomBrewerySettingsDivHTML;

    let beerlistBgColorSettingsDivHTML = `
        <div class="row border border-secondary rounded mb-2">
          <div class="col-2">
          `;
            beerlistBgColorSettingsDivHTML += colorOfEl("beerBgColorOne", screenSettings.beerBgColorOne, "Background Color #1:", "Background Color #1 Code:");
            beerlistBgColorSettingsDivHTML += `
          </div>
          <div class="col-2">
          `;
            beerlistBgColorSettingsDivHTML += colorOfEl("beerBgColorTwo", screenSettings.beerBgColorTwo, "Background Color #2:", "Background Color #2 Code:");
            beerlistBgColorSettingsDivHTML += `
          </div>
          <div class="col-2">
          `;
            beerlistBgColorSettingsDivHTML += colorOfEl("beerBgColorThree", screenSettings.beerBgColorThree, "Background Color #3:", "Background Color #3 Code:");
            beerlistBgColorSettingsDivHTML += `
          </div>
          <div class="col-2">
          `;
            beerlistBgColorSettingsDivHTML += colorOfEl("beerBgColorFour", screenSettings.beerBgColorFour, "Background Color #4:", "Background Color #4 Code:");
            beerlistBgColorSettingsDivHTML += `
          </div>
          <div class="col-2">
          `;
            beerlistBgColorSettingsDivHTML += colorOfEl("beerBgColorFive", screenSettings.beerBgColorFive, "Background Color #5:", "Background Color #5 Code:");
            beerlistBgColorSettingsDivHTML += `
          </div>
          <div class="col-2">
          `;
            beerlistBgColorSettingsDivHTML += colorDirectionEl(colorDirectionOptions, "beerBgColorDirection", screenSettings.beerBgColorDirection, "Background Font Color Direction");
            beerlistBgColorSettingsDivHTML += `
          </div>
        </div>
    `;
    beerscreenSettingsDiv.innerHTML += beerlistBgColorSettingsDivHTML;

    let beerNameFontSettingsDivHTML = `
        <div class="row border border-secondary rounded mb-2">
          <div class="col-2">
          `;
            beerNameFontSettingsDivHTML += fontOptionsEl(fontOptions, "beerNameFont", screenSettings.beerNameFont, "Beer Name Font");
            beerNameFontSettingsDivHTML += `
          </div>
          <div class="col-2">
          `;
            beerNameFontSettingsDivHTML += colorOfEl("beerNameFontColor", screenSettings.beerNameFontColor, "Beer Name Font Color:", "Beer Name Font Color code:");
            beerNameFontSettingsDivHTML += `
          </div>
          <div class="col-2">
          `;
            beerNameFontSettingsDivHTML += fontSizeOptionsEl(fontSizeOptions,"beerNameFontSize", screenSettings.beerNameFontSize, "Beer Name Font Size:");
            beerNameFontSettingsDivHTML += `
          </div>
          <div class="col-2">
          `;
            beerNameFontSettingsDivHTML += toggleSettingDiv("beerNameFontBoldToggle", screenSettings.beerNameFontBoldToggle, "Beer Name Bold:");
            beerNameFontSettingsDivHTML += `
          </div>
          <div class="col-2">
          `;
            beerNameFontSettingsDivHTML += toggleSettingDiv("beerNameFontItalicToggle", screenSettings.beerNameFontItalicToggle, "Beer Name Italic:");
            beerNameFontSettingsDivHTML += `
          </div>
          <div class="col-2">
          `;
            beerNameFontSettingsDivHTML += toggleSettingDiv("beerNameFontUnderlineToggle", screenSettings.beerNameFontUnderlineToggle, "Beer Name Underline:");
            beerNameFontSettingsDivHTML += `
          </div>
        </div>
    `;
    beerscreenSettingsDiv.innerHTML += beerNameFontSettingsDivHTML;

    let beerStyleFontSettingsDivHTML = `
        <div class="row border border-secondary rounded mb-2">
          <div class="col-2">
          `;
            beerStyleFontSettingsDivHTML += fontOptionsEl(fontOptions, "beerStyleFont", screenSettings.beerStyleFont, "Beer Style Font");
            beerStyleFontSettingsDivHTML += `
          </div>
          <div class="col-2">
          `;
            beerStyleFontSettingsDivHTML += colorOfEl("beerStyleFontColor", screenSettings.beerStyleFontColor, "Beer Style Font Color:", "Beer Style Font Color code:");
            beerStyleFontSettingsDivHTML += `
          </div>
          <div class="col-2">
          `;
            beerStyleFontSettingsDivHTML += fontSizeOptionsEl(fontSizeOptions,"beerStyleFontSize", screenSettings.beerStyleFontSize, "Beer Style Font Size:");
            beerStyleFontSettingsDivHTML += `
          </div>
          <div class="col-2">
          `;
            beerStyleFontSettingsDivHTML += toggleSettingDiv("beerStyleFontBoldToggle", screenSettings.beerStyleFontBoldToggle, "Beer Style Bold:");
            beerStyleFontSettingsDivHTML += `
          </div>
          <div class="col-2">
          `;
            beerStyleFontSettingsDivHTML += toggleSettingDiv("beerStyleFontItalicToggle", screenSettings.beerStyleFontItalicToggle, "Beer Style Italic:");
            beerStyleFontSettingsDivHTML += `
          </div>
          <div class="col-2">
          `;
            beerStyleFontSettingsDivHTML += toggleSettingDiv("beerStyleFontUnderlineToggle", screenSettings.beerStyleFontUnderlineToggle, "Beer Style Underline:");
            beerStyleFontSettingsDivHTML += `
          </div>
        </div>
    `;
    beerscreenSettingsDiv.innerHTML += beerStyleFontSettingsDivHTML;

    let beerAbvFontSettingsDivHTML = `
        <div class="row border border-secondary rounded mb-2">
          <div class="col-2">
            <div class="form-group">
            </div>
          </div>
          <div class="col-2">
          `;
            beerAbvFontSettingsDivHTML += colorOfEl("beerAbvFontColor", screenSettings.beerAbvFontColor, "Beer Abv Font Color:", "Beer Abv Font Color code:");
            beerAbvFontSettingsDivHTML += `
          </div>
          <div class="col-2">
          `;
            beerAbvFontSettingsDivHTML += fontSizeOptionsEl(fontSizeOptions,"beerAbvFontSize", screenSettings.beerAbvFontSize, "Beer Abv Font Size:");
            beerAbvFontSettingsDivHTML += `
          </div>
          <div class="col-2">
          `;
            beerAbvFontSettingsDivHTML += toggleSettingDiv("beerAbvFontBoldToggle", screenSettings.beerAbvFontBoldToggle, "Beer Abv Bold:");
            beerAbvFontSettingsDivHTML += `
          </div>
          <div class="col-2">
          `;
            beerAbvFontSettingsDivHTML += toggleSettingDiv("beerAbvFontItalicToggle", screenSettings.beerAbvFontItalicToggle, "Beer Abv Italic:");
            beerAbvFontSettingsDivHTML += `
          </div>
          <div class="col-2">
          `;
            beerAbvFontSettingsDivHTML += toggleSettingDiv("beerAbvFontUnderlineToggle", screenSettings.beerAbvFontUnderlineToggle, "Beer Abv Underline:");
            beerAbvFontSettingsDivHTML += `
          </div>
        </div>
    `;
    beerscreenSettingsDiv.innerHTML += beerAbvFontSettingsDivHTML;

    let beerIbuFontSettingsDivHTML = `
        <div class="row border border-secondary rounded mb-2">
          <div class="col-2">
            <div class="form-group">
            </div>
          </div>
          <div class="col-2">
            `;
            beerIbuFontSettingsDivHTML += colorOfEl("beerIbuFontColor", screenSettings.beerIbuFontColor, "Beer Ibu Font Color:", "Beer Ibu Font Color code:");
            beerIbuFontSettingsDivHTML += `
          </div>
          <div class="col-2">
          `;
            beerIbuFontSettingsDivHTML += fontSizeOptionsEl(fontSizeOptions,"beerIbuFontSize", screenSettings.beerIbuFontSize, "Beer Ibu Font Size:");
            beerIbuFontSettingsDivHTML += `
          </div>
          <div class="col-2">
          `;
            beerIbuFontSettingsDivHTML += toggleSettingDiv("beerIbuFontBoldToggle", screenSettings.beerIbuFontBoldToggle, "Beer Ibu Bold:");
            beerIbuFontSettingsDivHTML += `
          </div>
          <div class="col-2">
          `;
            beerIbuFontSettingsDivHTML += toggleSettingDiv("beerIbuFontItalicToggle", screenSettings.beerIbuFontItalicToggle, "Beer Ibu Italic:");
            beerIbuFontSettingsDivHTML += `
          </div>
          <div class="col-2">
          `;
            beerIbuFontSettingsDivHTML += toggleSettingDiv("beerIbuFontUnderlineToggle", screenSettings.beerIbuFontUnderlineToggle, "Beer Ibu Underline:");
            beerIbuFontSettingsDivHTML += `
          </div>
        </div>
    `;
    beerscreenSettingsDiv.innerHTML += beerIbuFontSettingsDivHTML;

    let beerBreweryFontSettingsDivHTML = `
        <div class="row border border-secondary rounded mb-2">
          <div class="col-2">
          `;
            beerBreweryFontSettingsDivHTML += fontOptionsEl(fontOptions, "beerBreweryFont", screenSettings.beerBreweryFont, "Beer Brewery Font:");
            beerBreweryFontSettingsDivHTML += `
          </div>
          <div class="col-2">
          `;
            beerBreweryFontSettingsDivHTML += colorOfEl("beerBreweryFontColor", screenSettings.beerBreweryFontColor, "Beer Brewery Font Color:", "Beer Brewery Font Color code:");
            beerBreweryFontSettingsDivHTML += `
          </div>
          <div class="col-2">
          `;
            beerBreweryFontSettingsDivHTML += fontSizeOptionsEl(fontSizeOptions,"beerBreweryFontSize", screenSettings.beerBreweryFontSize, "Beer Brewery Font Size:");
            beerBreweryFontSettingsDivHTML += `
          </div>
          <div class="col-2">
          `;
            beerBreweryFontSettingsDivHTML += toggleSettingDiv("beerBreweryFontBoldToggle", screenSettings.beerBreweryFontBoldToggle, "Beer Brewery Bold:");
            beerBreweryFontSettingsDivHTML += `
          </div>
          <div class="col-2">
          `;
            beerBreweryFontSettingsDivHTML += toggleSettingDiv("beerBreweryFontItalicToggle", screenSettings.beerBreweryFontItalicToggle, "Beer Brewery Italic:");
            beerBreweryFontSettingsDivHTML += `
          </div>
          <div class="col-2">
          `;
            beerBreweryFontSettingsDivHTML += toggleSettingDiv("beerBreweryFontUnderlineToggle", screenSettings.beerBreweryFontUnderlineToggle, "Beer Brewery Underline:");
            beerBreweryFontSettingsDivHTML += `
          </div>
        </div>
    `;
    beerscreenSettingsDiv.innerHTML += beerBreweryFontSettingsDivHTML;

    let tickerBgColorSettingsDivHTML = `
        <div class="row border border-secondary rounded mb-2">
          <div class="col-2">
          `;
            tickerBgColorSettingsDivHTML += colorOfEl("beerTickerBgColorOne", screenSettings.beerTickerBgColorOne, "Beer Ticker Background Color #1:", "Beer Ticker Background Color Code #1:");
            tickerBgColorSettingsDivHTML += `
          </div>
          <div class="col-2">
          `;
            tickerBgColorSettingsDivHTML += colorOfEl("beerTickerBgColorTwo", screenSettings.beerTickerBgColorTwo, "Beer Ticker Background Color #2:", "Beer Ticker Background Color Code #2:");
            tickerBgColorSettingsDivHTML += `
          </div>
          <div class="col-2">
          `;
            tickerBgColorSettingsDivHTML += colorOfEl("beerTickerBgColorThree", screenSettings.beerTickerBgColorThree, "Beer Ticker Background Color #3:", "Beer Ticker Background Color Code #3:");
            tickerBgColorSettingsDivHTML += `
          </div>
          <div class="col-2">
          `;
            tickerBgColorSettingsDivHTML += colorOfEl("beerTickerBgColorFour", screenSettings.beerTickerBgColorFour, "Beer Ticker Background Color #4:", "Beer Ticker Background Color Code #4:");
            tickerBgColorSettingsDivHTML += `
          </div>
          <div class="col-2">
          `;
            tickerBgColorSettingsDivHTML += colorOfEl("beerTickerBgColorFive", screenSettings.beerTickerBgColorFive, "Beer Ticker Background Color #5:", "Beer Ticker Background Color Code #5:");
            tickerBgColorSettingsDivHTML += `
          </div>
          <div class="col-2">
          `;
            tickerBgColorSettingsDivHTML += colorDirectionEl(colorDirectionOptions, "beerTickerBgColorDirection", screenSettings.beerTickerBgColorDirection, "Beer Ticker Background Font Color Direction:");
            tickerBgColorSettingsDivHTML += `
          </div>
        </div>
    `;
    beerscreenSettingsDiv.innerHTML += tickerBgColorSettingsDivHTML;

    let tickerSettingsDivHTML = `
        <div class="row border border-secondary rounded mb-2">
          <div class="col-2">
          `;
            tickerSettingsDivHTML += fontOptionsEl(fontOptions, "beerTickerBeernamesFont", screenSettings.beerTickerBeernamesFont, "Beer Ticker Names Font:");
            tickerSettingsDivHTML += `
          </div>
          <div class="col-2">
          `;
            tickerSettingsDivHTML += fontOptionsEl(fontOptions, "beerTickerFont", screenSettings.beerTickerFont, "Beer Ticker Font:");
            tickerSettingsDivHTML += `
          </div>
          <div class="col-2">
          `;
            tickerSettingsDivHTML += colorOfEl("beerTickerFontColor", screenSettings.beerTickerFontColor, "Beer Ticker Font Color:", "Beer Ticker FoCt Color Code:");
            tickerSettingsDivHTML += `
          </div>
          <div class="col-2">
          `;
            tickerSettingsDivHTML += fontSizeOptionsEl(fontSizeOptions,"beerTickerFontSize", screenSettings.beerTickerFontSize, "Beer Ticker Font Size:");
            tickerSettingsDivHTML += `
          </div>
          <div class="col-2">
          `;
            tickerSettingsDivHTML += toggleSettingDiv("beerTickerFontBoldToggle", screenSettings.beerTickerFontBoldToggle, "Beer Ticker Bold:");
            tickerSettingsDivHTML += `
          </div>
          <div class="col-2">
          `;
            tickerSettingsDivHTML += toggleSettingDiv("beerTickerFontItalicToggle", screenSettings.beerTickerFontItalicToggle, "Beer Ticker Italic:");
            tickerSettingsDivHTML += `
          </div>
          <div class="col-2">
          `;
            tickerSettingsDivHTML += toggleSettingDiv("beerTickerFontUnderlineToggle", screenSettings.beerTickerFontUnderlineToggle, "Beer Ticker Underline:");
            tickerSettingsDivHTML += `
          </div>
        </div>
    `;
    beerscreenSettingsDiv.innerHTML += tickerSettingsDivHTML;

    let tickerSettingsShowDivHTML = `
        <div class="row border border-secondary rounded mb-2">
          <div class="col-3">
          `;
            tickerSettingsShowDivHTML += toggleSettingDiv("beerTickerToggle", screenSettings.beerTickerToggle, "Show Beer Ticker:");
            tickerSettingsShowDivHTML += `
          </div>
          <div class="col-3">
            <label for="beerTickerScrollSpeed">Beer Ticker Scroll Speed:</label>
            <input class="form-control" id="beerTickerScrollSpeed" name="beerTickerScrollSpeed" required="" type="text" value="${ screenSettings.beerTickerScrollSpeed }">
          </div>
        </div>
    `;
    beerscreenSettingsDiv.innerHTML += tickerSettingsShowDivHTML;
  }




  repaintBeerscreenSettingsTemplate(displayData) {
    console.log(displayData);
    const { screenSettings, fontSizeOptions } = displayData;
    // console.log(screenSettings);
    // console.log(fontSizeOptions);
    let beerscreenSettingsDiv = document.querySelector('#beerscreen_settings');
    let colorDirectionOptions = ["to bottom", "to top", "to left", "to right", "to bottom left", "to bottom right", "to top left", "to top right"];
    let fontOptions = ["","Courier New", "Times Roman"];
    // let fontSizeOptions = ["", "1.0em", "1.5em", "2.0em", "2.5em", "3.0em", "3.5em", "4.0em", "4.5em", "5.0em", "5.5em", "6.0em"];

    const colorOfEl = (settingsId, setting, labelTxt1, labelTxt2) => {
      let divHTML = ``;
      let divFormGroupWrapper = [`<div class="form-group">`, `</div>`];
      let divLabel = ``;
      let divBody = ``;
      divHTML += divFormGroupWrapper[0];
      divLabel = `
        <label for="${ settingsId }">${ labelTxt1 }</label>
        <input id="${ settingsId }" class="form-control" name="${ settingsId }" type="color" value="${ setting }">
      `;
      divHTML += divLabel;
      divBody = `
        <label for="${ settingsId }">${ labelTxt2 }</label>
        <input class="form-control" disabled="" id="${ settingsId }" name="${ settingsId }" type="text" value="${ setting }">
      `;
      divHTML += divBody;
      divHTML += divFormGroupWrapper[1];
      return divHTML;
    };

    const toggleSettingDiv = (settingsId, settings, labelTxt) => {
      let divHTML;
      let divFormGroupWrapper = [`<div class="form-group">`, `</div>`];
      let divLabel = `<label for="${ settingsId }">${ labelTxt }</label>`;
      let divBody = ``;
      if ( settings ) {
        divBody += `
          <input class="form-control" id="${ settingsId }" checked="" name="${ settingsId }" type="checkbox" value="y">
        `;
      } else {
        divBody += `
          <input class="form-control" id="${ settingsId }" name="${ settingsId }" type="checkbox" value="y">
        `;
      }
      divHTML = divFormGroupWrapper[0];
      divHTML += divLabel;
      divHTML += divBody;
      divHTML += divFormGroupWrapper[1];
      return divHTML;
    };

    const fontOptionsEl = (options, settingsId, settings, labelTxt) => {
      let divHTML;
      let divFormGroupWrapper = [`<div class="form-group">`, `</div>`];
      let divLabel=`
        <label for="${ settingsId }">${labelTxt}</label>
        <select class="form-control" id="${ settingsId }" name="${ settingsId }">
      `;
      let divBody;
      divHTML = divFormGroupWrapper[0];
      divHTML += divLabel;
      options.forEach((option, index) => {
        // console.log(index, option, settings, settingsId);
        if (index == settings) {
          divBody += `
            <option selected="" value="${ index }">${ option }</option>
          `;
        } else if (index > 0) {
          divBody += `
            <option value="${ index }">${ option }</option>
          `;
        } else {}
      });
      divHTML += divBody;
      divHTML += `
        </select>
      `;
      divHTML += divFormGroupWrapper[1];
      return divHTML;
    };

    const fontSizeOptionsEl = fontOptionsEl;

    const colorDirectionEl = (options, settingsId, settings, labelTxt) => {
      let divHTML;
      let divFormGroupWrapper = [`<div class="form-group">`, `</div>`];
      let divLabel = `
        <label for="${ settingsId }">${labelTxt}</label>
        <select class="form-control" id="${ settingsId }" name="${ settingsId }">
      `;
      let divBody;
      divHTML = divFormGroupWrapper[0];
      divHTML += divLabel;
      options.forEach(option => {
        if (option == settings) {
          divBody += `
            <option selected="" value="${ option }">${ option }</option>
          `;
        } else {
          divBody += `
            <option value="${ option }">${ option }</option>
          `;
        }
      });
      divHTML += divBody;
      divHTML += `
        </select>
      `;
      divHTML += divFormGroupWrapper[1];
      return divHTML;
    };

    // console.log(beerscreenSettingsDiv);
    // beerscreenTemplate select
    // clear the beerscreenSettings UI
    beerscreenSettingsDiv.innerHTML = ``;

    beerscreenSettingsDiv.innerHTML += `
      <div class="accordion" id="accordionExample">
    `;


    // build screen ID select
    let beerscreenIdSelectHTML = `
      <div class="row border border-secondary rounded mb-2">
        <div class="col-6">
          <div class="form-group">
            <label for="beerscreenTemplate">Screen Template:</label>
            <select id="beerscreenTemplate" class="form-control" name="beerscreenTemplate">
              <option selected="" value="1">2 Columns, Name, ABV, IBU</option>
            </select>
          </div>
        </div>
        <div class="col-2">
        `;
          beerscreenIdSelectHTML += toggleSettingDiv("beerscreenLandscapePortraitToggle", screenSettings.beerscreenLandscapePortraitToggle, "Portrait:");
          beerscreenIdSelectHTML += `
        </div>
      </div>
    `;
    beerscreenSettingsDiv.innerHTML += beerscreenIdSelectHTML;

    let fontColorsDivHTML = `
      <div class="card">
        <div class="card-header" id="headingOne">
          <h2 class="mb-0">
            <button class="btn btn-link collapsed" type="button" data-toggle="collapse" data-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">
              <!-- Collapsible Group Item #1 -->
              <div class="d-flex justify-content-between col-12">
                <div>
                  <h3>Font Color</h3>
                </div>
                <div>
                  <h3>+</h3>
                </div>
              </div>
            </button>
          </h2>
        </div>
    `;
    fontColorsDivHTML += `
        <div id="collapseOne" class="collapse" aria-labelledby="headingOne" data-parent="#accordionExample">
          <div class="card-body">
                    <div class="row border border-secondary rounded mb-2">
                       <div class="col-12">
                       `;
                        fontColorsDivHTML += colorOfEl("fontColorOne", screenSettings.fontColorOne, "Font Color #1:", "Font Color Code #1:");
                        fontColorsDivHTML += `
                      `;
                        fontColorsDivHTML += colorOfEl("fontColorTwo", screenSettings.fontColorTwo, "Font Color #2:", "Font Color Code #2:");
                        fontColorsDivHTML += `
                      `;
                        fontColorsDivHTML += colorOfEl("fontColorThree", screenSettings.fontColorThree, "Font Color #3:", "Font Color Code #3:");
                        fontColorsDivHTML += `
                      `;
                        fontColorsDivHTML += colorDirectionEl(colorDirectionOptions, "fontColorDirection", screenSettings.fontColorDirection, "Font Color Direction:");
                        fontColorsDivHTML += `
                      </div>
                    </div>
          </div>
        </div>
      </div>
    `;
    beerscreenSettingsDiv.innerHTML += fontColorsDivHTML;

    let shadowFontColorHTML = `
      <div class="card">
        <div class="card-header" id="headingTwo">
          <h2 class="mb-0">
            <button class="btn btn-link collapsed" type="button" data-toggle="collapse" data-target="#collapseTwo" aria-expanded="false" aria-controls="collapseTwo">
              <!-- Collapsible Group Item #2 -->
              <div class="d-flex justify-content-between col-12">
                <div>
                  <h3>Shadow Font Color</h3>
                </div>
                <div>
                  <h3>+</h3>
                </div>
              </div>
            </button>
          </h2>
        </div>
    `;
    shadowFontColorHTML += `
        <div id="collapseTwo" class="collapse" aria-labelledby="headingTwo" data-parent="#accordionExample">
          <div class="card-body">
                        <div class="row border border-secondary rounded mb-2">
                          <div class="col-12">
                          `;
                            shadowFontColorHTML +=  colorOfEl("shadowFontColorOne", screenSettings.shadowFontColorOne, "Shadow Color #1:", "Shadow Color Code #1:");
                            shadowFontColorHTML += `
                          `;
                            shadowFontColorHTML += colorOfEl("shadowFontColorTwo", screenSettings.shadowFontColorTwo, "Shadow Color #2:", "Shadow Color Code #2:");
                            shadowFontColorHTML += `
                          `;
                            shadowFontColorHTML += colorOfEl("shadowFontColorThree", screenSettings.shadowFontColorThree, "Shadow Color #3:", "Shadow Color Code #3:");
                            shadowFontColorHTML += `
                          `;
                            shadowFontColorHTML += colorDirectionEl(colorDirectionOptions, "shadowFontColorDirection", screenSettings.shadowFontColorDirection, "Shadow Color Direction:")
                            shadowFontColorHTML += `
                          </div>
                        </div>
          </div>
        </div>
      </div>
    `;
    beerscreenSettingsDiv.innerHTML += shadowFontColorHTML;

    let bomBgColorDivHTML = `
      <div class="card">
        <div class="card-header" id="headingThree">
          <h2 class="mb-0">
            <button class="btn btn-link collapsed" type="button" data-toggle="collapse" data-target="#collapseThree" aria-expanded="false" aria-controls="collapseThree">
              <!-- Collapsible Group Item #3 -->
              <div class="d-flex justify-content-between col-12">
                <div>
                  <h3>Beer of the Month<br>Background Color</h3>
                </div>
                <div>
                  <h3>+</h3>
                </div>
              </div>
            </button>
          </h2>
        </div>
    `;
    bomBgColorDivHTML += `
        <div id="collapseThree" class="collapse" aria-labelledby="headingThree" data-parent="#accordionExample">
          <div class="card-body">
                        <div class="row border border-secondary rounded mb-2">
                          <div class="col-12">
                          `;
                            bomBgColorDivHTML += colorOfEl("beerBomBgColorOne", screenSettings.beerBomBgColorOne, "Beer of the Month Background Color #1:", "Beer of the Month Background Color Code #1:");
                            bomBgColorDivHTML += `
                          `;
                            bomBgColorDivHTML += colorOfEl("beerBomBgColorTwo", screenSettings.beerBomBgColorTwo, "Beer of the Month Background Color #2:", "Beer of the Month Background Color Code #2:");
                            bomBgColorDivHTML += `
                          `;
                            bomBgColorDivHTML += colorOfEl("beerBomBgColorThree", screenSettings.beerBomBgColorThree, "Beer of the Month Background Color #3:", "Beer of the Month Background Color Code #3:");
                            bomBgColorDivHTML += `
                          `;
                            bomBgColorDivHTML += colorOfEl("beerBomBgColorFour", screenSettings.beerBomBgColorFour, "Beer of the Month Background Color #4:", "Beer of the Month Background Color Code #4:");
                            bomBgColorDivHTML += `
                          `;
                            bomBgColorDivHTML += colorOfEl("beerBomBgColorFive", screenSettings.beerBomBgColorFive, "Beer of the Month Background Color #5:", "Beer of the Month Background Color Code #5:");
                            bomBgColorDivHTML += `
                          `;
                            bomBgColorDivHTML += colorDirectionEl(colorDirectionOptions, "beerBomBgColorDirection", screenSettings.beerBomBgColorDirection, "Beer of the Month Background Color Direction:");
                            bomBgColorDivHTML += `
                          </div>
                        </div>
          </div>
        </div>
      </div>
      `;
    beerscreenSettingsDiv.innerHTML += bomBgColorDivHTML;

    let bomNameSettingsDivHTML = `
      <div class="card">
        <div class="card-header" id="headingFour">
          <h2 class="mb-0">
            <button class="btn btn-link collapsed" type="button" data-toggle="collapse" data-target="#collapseFour" aria-expanded="false" aria-controls="collapseFour">
              <!-- Collapsible Group Item #4 -->
              <div class="d-flex justify-content-between col-12">
                <div>
                  <h3>Beer of the Month<br>Beer Name</h3>
                </div>
                <div>
                  <h3>+</h3>
                </div>
              </div>
            </button>
          </h2>
        </div>
    `;
    bomNameSettingsDivHTML += `
        <div id="collapseFour" class="collapse" aria-labelledby="headingFour" data-parent="#accordionExample">
          <div class="card-body">

                      <div class="row border border-secondary rounded mb-2">
                        <div class="col-12">
                        `;
                          bomNameSettingsDivHTML += fontOptionsEl(fontOptions, "beerBomNameFont",screenSettings.beerBomNameFont , "Beer of the Month Name Font:");
                          bomNameSettingsDivHTML += `
                        `;
                          bomNameSettingsDivHTML += colorOfEl("beerBomNameFontColor", screenSettings.beerBomNameFontColor, "Beer of the Month Name Font Color:", "Beer of the Month Name Font Color Code:");
                          bomNameSettingsDivHTML += `
                        `;
                          bomNameSettingsDivHTML += fontSizeOptionsEl(fontSizeOptions, "beerBomNameFontSize", screenSettings.beerBomNameFontSize, "Beer of the Month Name Font Size:");
                          bomNameSettingsDivHTML += `
                        `;
                          bomNameSettingsDivHTML += toggleSettingDiv("beerBomNameFontBoldToggle", screenSettings.beerBomNameFontBoldToggle, "Beer of the Month Name Bold:");
                          bomNameSettingsDivHTML += `
                        `;
                          bomNameSettingsDivHTML += toggleSettingDiv("beerBomNameFontItalicToggle", screenSettings.beerBomNameFontItalicToggle, "Beer of the Month Name Italic:");
                          bomNameSettingsDivHTML += `
                        `;
                          bomNameSettingsDivHTML += toggleSettingDiv("beerBomNameFontUnderlineToggle", screenSettings.beerBomNameFontUnderlineToggle, "Beer of the Month Name Underline:");
                          bomNameSettingsDivHTML += `
                        </div>
                      </div>
          </div>
        </div>
      </div>
    `;
    beerscreenSettingsDiv.innerHTML += bomNameSettingsDivHTML;

    let bomStyleSettingsDivHTML = `
      <div class="card">
        <div class="card-header" id="headingFive">
          <h2 class="mb-0">
            <button class="btn btn-link collapsed" type="button" data-toggle="collapse" data-target="#collapseFive" aria-expanded="false" aria-controls="collapseFive">
              <!-- Collapsible Group Item #5 -->
              <div class="d-flex justify-content-between col-12">
                <div>
                  <h3>Beer of the Month<br>Beer Style</h3>
                </div>
                <div>
                  <h3>+</h3>
                </div>
              </div>
            </button>
          </h2>
        </div>
    `;
    bomStyleSettingsDivHTML += `
        <div id="collapseFive" class="collapse" aria-labelledby="headingFive" data-parent="#accordionExample">
          <div class="card-body">
                        <div class="row border border-secondary rounded mb-2">
                          <div class="col-12">
                          `;
                            bomStyleSettingsDivHTML += fontOptionsEl(fontOptions, "beerBomStyleFont", screenSettings.beerBomStyleFont, "Beer of the Month Style Font:");
                            bomStyleSettingsDivHTML += `
                          `;
                            bomStyleSettingsDivHTML += colorOfEl("beerBomStyleFontColor", screenSettings.beerBomStyleFontColor, "Beer of the Month Style Font Color:", "Beer of the Month Style Font Color Code:");
                            bomStyleSettingsDivHTML += `
                          `;
                            bomStyleSettingsDivHTML += fontSizeOptionsEl(fontSizeOptions, "beerBomStyleFontSize", screenSettings.beerBomStyleFontSize, "Beer of the Month Style Font Size:");
                            bomStyleSettingsDivHTML += `
                          `;
                            bomStyleSettingsDivHTML += toggleSettingDiv("beerBomStyleFontBoldToggle", screenSettings.beerBomStyleFontBoldToggle, "Beer of the Month Style Bold:");
                            bomStyleSettingsDivHTML += `
                          `;
                            bomStyleSettingsDivHTML += toggleSettingDiv("beerBomStyleFontItalicToggle", screenSettings.beerBomStyleFontItalicToggle, "Beer of the Month Style Italic:");
                            bomStyleSettingsDivHTML += `
                          `;
                            bomStyleSettingsDivHTML += toggleSettingDiv("beerBomStyleFontUnderlineToggle", screenSettings.beerBomStyleFontUnderlineToggle, "Beer of the Month Style Underline:");
                            bomStyleSettingsDivHTML += `
                          </div>
                        </div>
          </div>
        </div>
      </div>
    `;
    beerscreenSettingsDiv.innerHTML += bomStyleSettingsDivHTML;

    let bomAbvSettingsDivHTML = `
      <div class="card">
        <div class="card-header" id="headingSix">
          <h2 class="mb-0">
            <button class="btn btn-link collapsed" type="button" data-toggle="collapse" data-target="#collapseSix" aria-expanded="false" aria-controls="collapseSix">
              <!-- Collapsible Group Item #6 -->
              <div class="d-flex justify-content-between col-12">
                <div>
                  <h3>Beer of the Month<br>Beer ABV</h3>
                </div>
                <div>
                  <h3>+</h3>
                </div>
              </div>
            </button>
          </h2>
        </div>
    `;

    bomAbvSettingsDivHTML += `
        <div id="collapseSix" class="collapse" aria-labelledby="headingSix" data-parent="#accordionExample">
          <div class="card-body">
                        <div class="row border border-secondary rounded mb-2">
                          <div class="col-12">
                            <div class="form-group">
                            </div>
                          </div>
                          <div class="col-12">
                          `;
                            bomAbvSettingsDivHTML += colorOfEl("beerBomAbvFontColor", screenSettings.beerBomAbvFontColor, "Beer of the Month Abv Font Color:", "Beer of the Month Abv Font Color Code:");
                            bomAbvSettingsDivHTML += `
                          </div>
                          <div class="col-12">
                          `;
                            bomAbvSettingsDivHTML += fontSizeOptionsEl(fontSizeOptions, "beerBomAbvFontSize", screenSettings.beerBomAbvFontSize, "Beer of the Month Abv Font Size:");
                            bomAbvSettingsDivHTML += `
                          </div>
                          <div class="col-12">
                          `;
                            bomAbvSettingsDivHTML += toggleSettingDiv("beerBomAbvFontBoldToggle", screenSettings.beerBomAbvFontBoldToggle, "Beer of the Month Abv Bold:");
                            bomAbvSettingsDivHTML += `
                          </div>
                          <div class="col-12">
                          `;
                            bomAbvSettingsDivHTML += toggleSettingDiv("beerBomAbvFontItalicToggle", screenSettings.beerBomAbvFontItalicToggle, "Beer of the Month Abv Italic:");
                            bomAbvSettingsDivHTML += `
                          </div>
                          <div class="col-12">
                          `;
                            bomAbvSettingsDivHTML += toggleSettingDiv("beerBomAbvFontUnderlineToggle", screenSettings.beerBomAbvFontUnderlineToggle, "Beer of the Month Abv Underline:");
                            bomAbvSettingsDivHTML += `
                          </div>
                        </div>
          </div>
        </div>
      </div>
    `;

    beerscreenSettingsDiv.innerHTML += bomAbvSettingsDivHTML;

    let bomIbuSettingsDivHTML = `
      <div class="card">
        <div class="card-header" id="headingSeven">
          <h2 class="mb-0">
            <button class="btn btn-link collapsed" type="button" data-toggle="collapse" data-target="#collapseSeven" aria-expanded="false" aria-controls="collapseSeven">
              <!-- Collapsible Group Item #7 -->
              <div class="d-flex justify-content-between col-12">
                <div>
                  <h3>Beer of the Month<br>Beer IBU</h3>
                </div>
                <div>
                  <h3>+</h3>
                </div>
              </div>
            </button>
          </h2>
        </div>
    `;
    bomIbuSettingsDivHTML += `
        <div id="collapseSeven" class="collapse" aria-labelledby="headingSeven" data-parent="#accordionExample">
          <div class="card-body">
                    <div class="row border border-secondary rounded mb-2">
                      <div class="col-12">
                        <div class="form-group">
                        </div>
                      </div>
                      <div class="col-12">
                      `;
                        bomIbuSettingsDivHTML += colorOfEl("beerBomIbuFontColor", screenSettings.beerBomIbuFontColor, "Beer of the Month Ibu Font Color:", "Beer of the Month Ibu Font Color Code:");
                        bomIbuSettingsDivHTML += `
                      </div>
                      <div class="col-12">
                      `;
                        bomIbuSettingsDivHTML += fontSizeOptionsEl(fontSizeOptions,"beerBomIbuFontSize", screenSettings.beerBomIbuFontSize, "Beer of the Month Ibu Font Size:");
                        bomIbuSettingsDivHTML += `
                      </div>
                      <div class="col-12">
                      `;
                        bomIbuSettingsDivHTML += toggleSettingDiv("beerBomIbuFontBoldToggle", screenSettings.beerBomIbuFontBoldToggle, "Beer of the Month Ibu Bold:");
                        bomIbuSettingsDivHTML += `
                      </div>
                      <div class="col-12">
                      `;
                        bomIbuSettingsDivHTML += toggleSettingDiv("beerBomIbuFontItalicToggle", screenSettings.beerBomIbuFontItalicToggle, "Beer of the Month Ibu Italic:");
                        bomIbuSettingsDivHTML += `
                      </div>
                      <div class="col-12">
                      `;
                        bomIbuSettingsDivHTML += toggleSettingDiv("beerBomIbuFontUnderlineToggle", screenSettings.beerBomIbuFontUnderlineToggle, "Beer of the Month Ibu Underline:");
                        bomIbuSettingsDivHTML += `
                      </div>
                    </div>
          </div>
        </div>
      </div>
    `;
    beerscreenSettingsDiv.innerHTML += bomIbuSettingsDivHTML;

    let bomBrewerySettingsDivHTML = `
      <div class="card">
        <div class="card-header" id="headingEight">
          <h2 class="mb-0">
            <button class="btn btn-link collapsed" type="button" data-toggle="collapse" data-target="#collapseEight" aria-expanded="false" aria-controls="collapseEight">
              <!-- Collapsible Group Item #8 -->
              <div class="d-flex justify-content-between col-12">
                <div>
                  <h3>Beer of the Month<br>Beer Brewery</h3>
                </div>
                <div>
                  <h3>+</h3>
                </div>
              </div>
            </button>
          </h2>
        </div>
    `;
    bomBrewerySettingsDivHTML += `
        <div id="collapseEight" class="collapse" aria-labelledby="headingEight" data-parent="#accordionExample">
          <div class="card-body">
                        <div class="row border border-secondary rounded mb-2">
                          <div class="col-12">
                        `;
                        bomBrewerySettingsDivHTML += fontOptionsEl(fontOptions, "beerBomBreweryFont", screenSettings.beerBomBreweryFont, "Beer of the Month Brewery Font");
                        bomBrewerySettingsDivHTML += `
                          </div>
                          <div class="col-12">
                            `;
                        bomBrewerySettingsDivHTML +=  colorOfEl("beerBomBreweryFontColor", screenSettings.beerBomBreweryFontColor, "Beer of the Month Brewery Font Color:", "Beer of the Month Brewery Font Color Code:");
                        bomBrewerySettingsDivHTML += `
                          </div>
                          <div class="col-12">
                        `;
                        bomBrewerySettingsDivHTML += fontSizeOptionsEl(fontSizeOptions,"beerBomBreweryFontSize", screenSettings.beerBomBreweryFontSize, "Beer of the Month Brewery Font Size:");
                        bomBrewerySettingsDivHTML += `
                          </div>
                          <div class="col-12">
                        `;
                        bomBrewerySettingsDivHTML += toggleSettingDiv("beerBomBreweryFontBoldToggle", screenSettings.beerBomBreweryFontBoldToggle, "Beer of the Month Brewery Bold:");
                        bomBrewerySettingsDivHTML += `
                          </div>
                          <div class="col-12">
                        `;
                        bomBrewerySettingsDivHTML += toggleSettingDiv("beerBomBreweryFontItalicToggle", screenSettings.beerBomBreweryFontItalicToggle, "Beer of the Month Brewery Italic:");
                        bomBrewerySettingsDivHTML += `
                          </div>
                          <div class="col-12">
                        `;
                        bomBrewerySettingsDivHTML += toggleSettingDiv("beerBomBreweryFontUnderlineToggle", screenSettings.beerBomBreweryFontUnderlineToggle, "Beer of the Month Brewery Underline:");
                        bomBrewerySettingsDivHTML += `
                          </div>
                        </div>
          </div>
        </div>
      </div>
    `;
    beerscreenSettingsDiv.innerHTML += bomBrewerySettingsDivHTML;

    let beerlistBgColorSettingsDivHTML = `
      <div class="card">
        <div class="card-header" id="headingNine">
          <h2 class="mb-0">
            <button class="btn btn-link collapsed" type="button" data-toggle="collapse" data-target="#collapseNine" aria-expanded="false" aria-controls="collapseNine">
              <!-- Collapsible Group Item #9 -->
              <div class="d-flex justify-content-between col-12">
                <div>
                  <h3>Beer Background Color</h3>
                </div>
                <div>
                  <h3>+</h3>
                </div>
              </div>
            </button>
          </h2>
        </div>
    `;
    beerlistBgColorSettingsDivHTML += `
        <div id="collapseNine" class="collapse" aria-labelledby="headingNine" data-parent="#accordionExample">
          <div class="card-body">
                        <div class="row border border-secondary rounded mb-2">
                          <div class="col-12">
                          `;
                            beerlistBgColorSettingsDivHTML += colorOfEl("beerBgColorOne", screenSettings.beerBgColorOne, "Background Color #1:", "Background Color #1 Code:");
                            beerlistBgColorSettingsDivHTML += `
                          </div>
                          <div class="col-12">
                          `;
                            beerlistBgColorSettingsDivHTML += colorOfEl("beerBgColorTwo", screenSettings.beerBgColorTwo, "Background Color #2:", "Background Color #2 Code:");
                            beerlistBgColorSettingsDivHTML += `
                          </div>
                          <div class="col-12">
                          `;
                            beerlistBgColorSettingsDivHTML += colorOfEl("beerBgColorThree", screenSettings.beerBgColorThree, "Background Color #3:", "Background Color #3 Code:");
                            beerlistBgColorSettingsDivHTML += `
                          </div>
                          <div class="col-12">
                          `;
                            beerlistBgColorSettingsDivHTML += colorOfEl("beerBgColorFour", screenSettings.beerBgColorFour, "Background Color #4:", "Background Color #4 Code:");
                            beerlistBgColorSettingsDivHTML += `
                          </div>
                          <div class="col-12">
                          `;
                            beerlistBgColorSettingsDivHTML += colorOfEl("beerBgColorFive", screenSettings.beerBgColorFive, "Background Color #5:", "Background Color #5 Code:");
                            beerlistBgColorSettingsDivHTML += `
                          </div>
                          <div class="col-12">
                          `;
                            beerlistBgColorSettingsDivHTML += colorDirectionEl(colorDirectionOptions, "beerBgColorDirection", screenSettings.beerBgColorDirection, "Background Font Color Direction");
                            beerlistBgColorSettingsDivHTML += `
                          </div>
                        </div>
          </div>
        </div>
      </div>
    `;
    beerscreenSettingsDiv.innerHTML += beerlistBgColorSettingsDivHTML;

    let beerNameFontSettingsDivHTML = `
      <div class="card">
        <div class="card-header" id="headingTen">
          <h2 class="mb-0">
            <button class="btn btn-link collapsed" type="button" data-toggle="collapse" data-target="#collapseTen" aria-expanded="false" aria-controls="collapseTen">
              <!-- Collapsible Group Item #10 -->
              <div class="d-flex justify-content-between col-12">
                <div>
                  <h3>Beer Name</h3>
                </div>
                <div>
                  <h3>+</h3>
                </div>
              </div>
            </button>
          </h2>
        </div>
    `;
    beerNameFontSettingsDivHTML += `
        <div id="collapseTen" class="collapse" aria-labelledby="headingTen" data-parent="#accordionExample">
          <div class="card-body">
                        <div class="row border border-secondary rounded mb-2">
                          <div class="col-12">
                          `;
                            beerNameFontSettingsDivHTML += fontOptionsEl(fontOptions, "beerNameFont", screenSettings.beerNameFont, "Beer Name Font");
                            beerNameFontSettingsDivHTML += `
                          </div>
                          <div class="col-12">
                          `;
                            beerNameFontSettingsDivHTML += colorOfEl("beerNameFontColor", screenSettings.beerNameFontColor, "Beer Name Font Color:", "Beer Name Font Color code:");
                            beerNameFontSettingsDivHTML += `
                          </div>
                          <div class="col-12">
                          `;
                            beerNameFontSettingsDivHTML += fontSizeOptionsEl(fontSizeOptions,"beerNameFontSize", screenSettings.beerNameFontSize, "Beer Name Font Size:");
                            beerNameFontSettingsDivHTML += `
                          </div>
                          <div class="col-12">
                          `;
                            beerNameFontSettingsDivHTML += toggleSettingDiv("beerNameFontBoldToggle", screenSettings.beerNameFontBoldToggle, "Beer Name Bold:");
                            beerNameFontSettingsDivHTML += `
                          </div>
                          <div class="col-12">
                          `;
                            beerNameFontSettingsDivHTML += toggleSettingDiv("beerNameFontItalicToggle", screenSettings.beerNameFontItalicToggle, "Beer Name Italic:");
                            beerNameFontSettingsDivHTML += `
                          </div>
                          <div class="col-12">
                          `;
                            beerNameFontSettingsDivHTML += toggleSettingDiv("beerNameFontUnderlineToggle", screenSettings.beerNameFontUnderlineToggle, "Beer Name Underline:");
                            beerNameFontSettingsDivHTML += `
                          </div>
                        </div>
          </div>
        </div>
      </div>
    `;
    beerscreenSettingsDiv.innerHTML += beerNameFontSettingsDivHTML;

    let beerStyleFontSettingsDivHTML = `
      <div class="card">
        <div class="card-header" id="headingEleven">
          <h2 class="mb-0">
            <button class="btn btn-link collapsed" type="button" data-toggle="collapse" data-target="#collapseEleven" aria-expanded="false" aria-controls="collapseEleven">
              <!-- Collapsible Group Item #11 -->
              <div class="d-flex justify-content-between col-12">
                <div>
                  <h3>Beer Style</h3>
                </div>
                <div>
                  <h3>+</h3>
                </div>
              </div>
            </button>
          </h2>
        </div>
    `;
    beerStyleFontSettingsDivHTML += `
        <div id="collapseEleven" class="collapse" aria-labelledby="headingEleven" data-parent="#accordionExample">
          <div class="card-body">
                        <div class="row border border-secondary rounded mb-2">
                          <div class="col-12">
                          `;
                            beerStyleFontSettingsDivHTML += fontOptionsEl(fontOptions, "beerStyleFont", screenSettings.beerStyleFont, "Beer Style Font");
                            beerStyleFontSettingsDivHTML += `
                          </div>
                          <div class="col-12">
                          `;
                            beerStyleFontSettingsDivHTML += colorOfEl("beerStyleFontColor", screenSettings.beerStyleFontColor, "Beer Style Font Color:", "Beer Style Font Color code:");
                            beerStyleFontSettingsDivHTML += `
                          </div>
                          <div class="col-12">
                          `;
                            beerStyleFontSettingsDivHTML += fontSizeOptionsEl(fontSizeOptions,"beerStyleFontSize", screenSettings.beerStyleFontSize, "Beer Style Font Size:");
                            beerStyleFontSettingsDivHTML += `
                          </div>
                          <div class="col-12">
                          `;
                            beerStyleFontSettingsDivHTML += toggleSettingDiv("beerStyleFontBoldToggle", screenSettings.beerStyleFontBoldToggle, "Beer Style Bold:");
                            beerStyleFontSettingsDivHTML += `
                          </div>
                          <div class="col-12">
                          `;
                            beerStyleFontSettingsDivHTML += toggleSettingDiv("beerStyleFontItalicToggle", screenSettings.beerStyleFontItalicToggle, "Beer Style Italic:");
                            beerStyleFontSettingsDivHTML += `
                          </div>
                          <div class="col-12">
                          `;
                            beerStyleFontSettingsDivHTML += toggleSettingDiv("beerStyleFontUnderlineToggle", screenSettings.beerStyleFontUnderlineToggle, "Beer Style Underline:");
                            beerStyleFontSettingsDivHTML += `
                          </div>
                        </div>
          </div>
        </div>
      </div>
    `;
    beerscreenSettingsDiv.innerHTML += beerStyleFontSettingsDivHTML;

    let beerAbvFontSettingsDivHTML = `
      <div class="card">
        <div class="card-header" id="headingTwelve">
          <h2 class="mb-0">
            <button class="btn btn-link collapsed" type="button" data-toggle="collapse" data-target="#collapseTwelve" aria-expanded="false" aria-controls="collapseTwelve">
              <!-- Collapsible Group Item #12 -->
              <div class="d-flex justify-content-between col-12">
                <div>
                  <h3>Beer ABV</h3>
                </div>
                <div>
                  <h3>+</h3>
                </div>
              </div>
            </button>
          </h2>
        </div>
    `;
    beerAbvFontSettingsDivHTML += `
        <div id="collapseTwelve" class="collapse" aria-labelledby="headingTwelve" data-parent="#accordionExample">
          <div class="card-body">
                        <div class="row border border-secondary rounded mb-2">
                          <div class="col-12">
                            <div class="form-group">
                            </div>
                          </div>
                          <div class="col-12">
                          `;
                            beerAbvFontSettingsDivHTML += colorOfEl("beerAbvFontColor", screenSettings.beerAbvFontColor, "Beer Abv Font Color:", "Beer Abv Font Color code:");
                            beerAbvFontSettingsDivHTML += `
                          </div>
                          <div class="col-12">
                          `;
                            beerAbvFontSettingsDivHTML += fontSizeOptionsEl(fontSizeOptions,"beerAbvFontSize", screenSettings.beerAbvFontSize, "Beer Abv Font Size:");
                            beerAbvFontSettingsDivHTML += `
                          </div>
                          <div class="col-12">
                          `;
                            beerAbvFontSettingsDivHTML += toggleSettingDiv("beerAbvFontBoldToggle", screenSettings.beerAbvFontBoldToggle, "Beer Abv Bold:");
                            beerAbvFontSettingsDivHTML += `
                          </div>
                          <div class="col-12">
                          `;
                            beerAbvFontSettingsDivHTML += toggleSettingDiv("beerAbvFontItalicToggle", screenSettings.beerAbvFontItalicToggle, "Beer Abv Italic:");
                            beerAbvFontSettingsDivHTML += `
                          </div>
                          <div class="col-12">
                          `;
                            beerAbvFontSettingsDivHTML += toggleSettingDiv("beerAbvFontUnderlineToggle", screenSettings.beerAbvFontUnderlineToggle, "Beer Abv Underline:");
                            beerAbvFontSettingsDivHTML += `
                          </div>
                        </div>
          </div>
        </div>
      </div>
    `;
    beerscreenSettingsDiv.innerHTML += beerAbvFontSettingsDivHTML;

    let beerIbuFontSettingsDivHTML = `
      <div class="card">
        <div class="card-header" id="headingThirteen">
          <h2 class="mb-0">
            <button class="btn btn-link collapsed" type="button" data-toggle="collapse" data-target="#collapseThirteen" aria-expanded="false" aria-controls="collapseThirteen">
              <!-- Collapsible Group Item #13 -->
              <div class="d-flex justify-content-between col-12">
                <div>
                  <h3>Beer IBU</h3>
                </div>
                <div>
                  <h3>+</h3>
                </div>
              </div>
            </button>
          </h2>
        </div>
    `;
    beerIbuFontSettingsDivHTML += `
        <div id="collapseThirteen" class="collapse" aria-labelledby="headingThirteen" data-parent="#accordionExample">
          <div class="card-body">
                        <div class="row border border-secondary rounded mb-2">
                          <div class="col-12">
                            <div class="form-group">
                            </div>
                          </div>
                          <div class="col-12">
                            `;
                            beerIbuFontSettingsDivHTML += colorOfEl("beerIbuFontColor", screenSettings.beerIbuFontColor, "Beer Ibu Font Color:", "Beer Ibu Font Color code:");
                            beerIbuFontSettingsDivHTML += `
                          </div>
                          <div class="col-12">
                          `;
                            beerIbuFontSettingsDivHTML += fontSizeOptionsEl(fontSizeOptions,"beerIbuFontSize", screenSettings.beerIbuFontSize, "Beer Ibu Font Size:");
                            beerIbuFontSettingsDivHTML += `
                          </div>
                          <div class="col-12">
                          `;
                            beerIbuFontSettingsDivHTML += toggleSettingDiv("beerIbuFontBoldToggle", screenSettings.beerIbuFontBoldToggle, "Beer Ibu Bold:");
                            beerIbuFontSettingsDivHTML += `
                          </div>
                          <div class="col-12">
                          `;
                            beerIbuFontSettingsDivHTML += toggleSettingDiv("beerIbuFontItalicToggle", screenSettings.beerIbuFontItalicToggle, "Beer Ibu Italic:");
                            beerIbuFontSettingsDivHTML += `
                          </div>
                          <div class="col-12">
                          `;
                            beerIbuFontSettingsDivHTML += toggleSettingDiv("beerIbuFontUnderlineToggle", screenSettings.beerIbuFontUnderlineToggle, "Beer Ibu Underline:");
                            beerIbuFontSettingsDivHTML += `
                          </div>
                        </div>
          </div>
        </div>
      </div>
    `;
    beerscreenSettingsDiv.innerHTML += beerIbuFontSettingsDivHTML;

    let beerBreweryFontSettingsDivHTML = `
      <div class="card">
        <div class="card-header" id="headingFourteen">
          <h2 class="mb-0">
            <button class="btn btn-link collapsed" type="button" data-toggle="collapse" data-target="#collapseFourteen" aria-expanded="false" aria-controls="collapseFourteen">
              <!-- Collapsible Group Item #14 -->
              <div class="d-flex justify-content-between col-12">
                <div>
                  <h3>Beer Brewery</h3>
                </div>
                <div>
                  <h3>+</h3>
                </div>
              </div>
            </button>
          </h2>
        </div>
    `;
    beerBreweryFontSettingsDivHTML += `
        <div id="collapseFourteen" class="collapse" aria-labelledby="headingFourteen" data-parent="#accordionExample">
          <div class="card-body">
                        <div class="row border border-secondary rounded mb-2">
                          <div class="col-12">
                          `;
                            beerBreweryFontSettingsDivHTML += fontOptionsEl(fontOptions, "beerBreweryFont", screenSettings.beerBreweryFont, "Beer Brewery Font:");
                            beerBreweryFontSettingsDivHTML += `
                          </div>
                          <div class="col-12">
                          `;
                            beerBreweryFontSettingsDivHTML += colorOfEl("beerBreweryFontColor", screenSettings.beerBreweryFontColor, "Beer Brewery Font Color:", "Beer Brewery Font Color code:");
                            beerBreweryFontSettingsDivHTML += `
                          </div>
                          <div class="col-12">
                          `;
                            beerBreweryFontSettingsDivHTML += fontSizeOptionsEl(fontSizeOptions,"beerBreweryFontSize", screenSettings.beerBreweryFontSize, "Beer Brewery Font Size:");
                            beerBreweryFontSettingsDivHTML += `
                          </div>
                          <div class="col-12">
                          `;
                            beerBreweryFontSettingsDivHTML += toggleSettingDiv("beerBreweryFontBoldToggle", screenSettings.beerBreweryFontBoldToggle, "Beer Brewery Bold:");
                            beerBreweryFontSettingsDivHTML += `
                          </div>
                          <div class="col-12">
                          `;
                            beerBreweryFontSettingsDivHTML += toggleSettingDiv("beerBreweryFontItalicToggle", screenSettings.beerBreweryFontItalicToggle, "Beer Brewery Italic:");
                            beerBreweryFontSettingsDivHTML += `
                          </div>
                          <div class="col-12">
                          `;
                            beerBreweryFontSettingsDivHTML += toggleSettingDiv("beerBreweryFontUnderlineToggle", screenSettings.beerBreweryFontUnderlineToggle, "Beer Brewery Underline:");
                            beerBreweryFontSettingsDivHTML += `
                          </div>
                        </div>
          </div>
        </div>
      </div>
    `;
    beerscreenSettingsDiv.innerHTML += beerBreweryFontSettingsDivHTML;

    let tickerBgColorSettingsDivHTML = `
      <div class="card">
        <div class="card-header" id="headingFifteen">
          <h2 class="mb-0">
            <button class="btn btn-link collapsed" type="button" data-toggle="collapse" data-target="#collapseFifteen" aria-expanded="false" aria-controls="collapseFifteen">
              <!-- Collapsible Group Item #15 -->
              <div class="d-flex justify-content-between col-12">
                <div>
                  <h3>Beer Ticker Background</h3>
                </div>
                <div>
                  <h3>+</h3>
                </div>
              </div>
            </button>
          </h2>
        </div>
    `;
    tickerBgColorSettingsDivHTML += `
        <div id="collapseFifteen" class="collapse" aria-labelledby="headingFifteen" data-parent="#accordionExample">
          <div class="card-body">
                        <div class="row border border-secondary rounded mb-2">
                          <div class="col-12">
                          `;
                            tickerBgColorSettingsDivHTML += colorOfEl("beerTickerBgColorOne", screenSettings.beerTickerBgColorOne, "Beer Ticker Background Color #1:", "Beer Ticker Background Color Code #1:");
                            tickerBgColorSettingsDivHTML += `
                          </div>
                          <div class="col-12">
                          `;
                            tickerBgColorSettingsDivHTML += colorOfEl("beerTickerBgColorTwo", screenSettings.beerTickerBgColorTwo, "Beer Ticker Background Color #2:", "Beer Ticker Background Color Code #2:");
                            tickerBgColorSettingsDivHTML += `
                          </div>
                          <div class="col-12">
                          `;
                            tickerBgColorSettingsDivHTML += colorOfEl("beerTickerBgColorThree", screenSettings.beerTickerBgColorThree, "Beer Ticker Background Color #3:", "Beer Ticker Background Color Code #3:");
                            tickerBgColorSettingsDivHTML += `
                          </div>
                          <div class="col-12">
                          `;
                            tickerBgColorSettingsDivHTML += colorOfEl("beerTickerBgColorFour", screenSettings.beerTickerBgColorFour, "Beer Ticker Background Color #4:", "Beer Ticker Background Color Code #4:");
                            tickerBgColorSettingsDivHTML += `
                          </div>
                          <div class="col-12">
                          `;
                            tickerBgColorSettingsDivHTML += colorOfEl("beerTickerBgColorFive", screenSettings.beerTickerBgColorFive, "Beer Ticker Background Color #5:", "Beer Ticker Background Color Code #5:");
                            tickerBgColorSettingsDivHTML += `
                          </div>
                          <div class="col-12">
                          `;
                            tickerBgColorSettingsDivHTML += colorDirectionEl(colorDirectionOptions, "beerTickerBgColorDirection", screenSettings.beerTickerBgColorDirection, "Beer Ticker Background Font Color Direction:");
                            tickerBgColorSettingsDivHTML += `
                          </div>
                        </div>
          </div>
        </div>
      </div>
    `;
    beerscreenSettingsDiv.innerHTML += tickerBgColorSettingsDivHTML;

    let tickerSettingsDivHTML = `
      <div class="card">
        <div class="card-header" id="headingSixteen">
          <h2 class="mb-0">
            <button class="btn btn-link collapsed" type="button" data-toggle="collapse" data-target="#collapseSixteen" aria-expanded="false" aria-controls="collapseSixteen">
              <!-- Collapsible Group Item #16 -->
              <div class="d-flex justify-content-between col-12">
                <div>
                  <h3>Beer Ticker</h3>
                </div>
                <div>
                  <h3>+</h3>
                </div>
              </div>
            </button>
          </h2>
        </div>
    `;
    tickerSettingsDivHTML += `
        <div id="collapseSixteen" class="collapse" aria-labelledby="headingSixteen" data-parent="#accordionExample">
          <div class="card-body">
                        <div class="row border border-secondary rounded mb-2">
                          <div class="col-12">
                          `;
                            tickerSettingsDivHTML += fontOptionsEl(fontOptions, "beerTickerBeernamesFont", screenSettings.beerTickerBeernamesFont, "Beer Ticker Names Font:");
                            tickerSettingsDivHTML += `
                          </div>
                          <div class="col-12">
                          `;
                            tickerSettingsDivHTML += fontOptionsEl(fontOptions, "beerTickerFont", screenSettings.beerTickerFont, "Beer Ticker Font:");
                            tickerSettingsDivHTML += `
                          </div>
                          <div class="col-12">
                          `;
                            tickerSettingsDivHTML += colorOfEl("beerTickerFontColor", screenSettings.beerTickerFontColor, "Beer Ticker Font Color:", "Beer Ticker FoCt Color Code:");
                            tickerSettingsDivHTML += `
                          </div>
                          <div class="col-12">
                          `;
                            tickerSettingsDivHTML += fontSizeOptionsEl(fontSizeOptions,"beerTickerFontSize", screenSettings.beerTickerFontSize, "Beer Ticker Font Size:");
                            tickerSettingsDivHTML += `
                          </div>
                          <div class="col-12">
                          `;
                            tickerSettingsDivHTML += toggleSettingDiv("beerTickerFontBoldToggle", screenSettings.beerTickerFontBoldToggle, "Beer Ticker Bold:");
                            tickerSettingsDivHTML += `
                          </div>
                          <div class="col-12">
                          `;
                            tickerSettingsDivHTML += toggleSettingDiv("beerTickerFontItalicToggle", screenSettings.beerTickerFontItalicToggle, "Beer Ticker Italic:");
                            tickerSettingsDivHTML += `
                          </div>
                          <div class="col-12">
                          `;
                            tickerSettingsDivHTML += toggleSettingDiv("beerTickerFontUnderlineToggle", screenSettings.beerTickerFontUnderlineToggle, "Beer Ticker Underline:");
                            tickerSettingsDivHTML += `
                          </div>
                        </div>
          </div>
        </div>
      </div>
    `;
    beerscreenSettingsDiv.innerHTML += tickerSettingsDivHTML;

    let tickerSettingsShowDivHTML = `
      <div class="card">
        <div class="card-header" id="headingSeventeen">
          <h2 class="mb-0">
            <button class="btn btn-link collapsed" type="button" data-toggle="collapse" data-target="#collapseSeventeen" aria-expanded="false" aria-controls="collapseSeventeen">
              <!-- Collapsible Group Item #17 -->
              <div class="d-flex justify-content-between col-12">
                <div>
                  <h3>Beer Ticker Settings</h3>
                </div>
                <div>
                  <h3>+</h3>
                </div>
              </div>
            </button>
          </h2>
        </div>
    `;
    tickerSettingsShowDivHTML += `
        <div id="collapseSeventeen" class="collapse" aria-labelledby="headingSeventeen" data-parent="#accordionExample">
          <div class="card-body">
                        <div class="row border border-secondary rounded mb-2">
                          <div class="col-3">
                          `;
                            tickerSettingsShowDivHTML += toggleSettingDiv("beerTickerToggle", screenSettings.beerTickerToggle, "Show Beer Ticker:");
                            tickerSettingsShowDivHTML += `
                          </div>
                          <div class="col-3">
                            <label for="beerTickerScrollSpeed">Beer Ticker Scroll Speed:</label>
                            <input class="form-control" id="beerTickerScrollSpeed" name="beerTickerScrollSpeed" required="" type="text" value="${ screenSettings.beerTickerScrollSpeed }">
                          </div>
                        </div>
          </div>
        </div>
      </div>
    `;
    beerscreenSettingsDiv.innerHTML += tickerSettingsShowDivHTML;

    // END ACCORDION DIV
    beerscreenSettingsDiv.innerHTML += `
      </div>
    `;
  }
}
