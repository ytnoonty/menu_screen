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
        name.style.fontSize = `${settings.beerNameFontSize}`;
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
        style.style.fontSize = `${settings.beerStyleFontSize}`;
      });

      beerAbvs.forEach(abv => {
        abv.style.color = `${settings.beerAbvFontColor}`;
        abv.style.fontSize = `${settings.beerAbvFontSize}`;
      });

      beerBrewerys.forEach(brewery => {
        brewery.style.color = `${settings.beerBreweryFontColor}`;
        brewery.style.fontSize = `${settings.beerBreweryFontSize}`;
      });

      backgrounds.forEach(background => {
        background.style.backgroundImage = `linear-gradient(${settings.beerBgColorDirection}, ${settings.beerBgColorOne}, ${settings.beerBgColorTwo}, ${settings.beerBgColorThree}, ${settings.beerBgColorFour}, ${settings.beerBgColorFive})`;
      });

      bomBackgrounds.forEach(background => {
        background.style.backgroundImage = `linear-gradient(${settings.beerBomBgColorDirection}, ${settings.beerBomBgColorOne}, ${settings.beerBomBgColorTwo},${settings.beerBomBgColorThree}, ${settings.beerBomBgColorFour}, ${settings.beerBomBgColorFive})`;
      });

      tickerText.forEach(text => {
        text.style.color = `${settings.beerTickerFontColor}`;
        text.style.fontSize = `${settings.beerTickerFontSize}`;
      });
      tickerNews.forEach(news => {
        news.style.color = `${settings.beerTickerFontColor}`;
        news.style.fontSize = `${settings.beerTickerFontSize}`;
      });

      tickerWrapper.style.backgroundImage = `linear-gradient(${settings.beerTickerBgColorDirection}, ${settings.beerTickerBgColorOne}, ${settings.beerTickerBgColorTwo},${settings.beerTickerBgColorThree}, ${settings.beerTickerBgColorFour}, ${settings.beerTickerBgColorFive})`;

      (function(Ticker, settings, tickerWrapper){
        const ticker = Ticker();
        ticker.callLoadTicker(settings, tickerWrapper);
        ticker.callMoveTicker(settings);

      })(Ticker, settings, tickerWrapper);


    } //END updateScreenTemplates


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
                              console.log("/////////////////////////////////////////////////////////////////");
                              console.log("/////////////////////////////////////////////////////////////////");
                              console.log("/////////////////////////////////////////////////////////////////");
                              console.log('CHANGED TO A DIFFERENT SCREEN FROM EDIT BEERLIST SCREEN');
                              console.log(data);
                              console.log("/////////////////////////////////////////////////////////////////");
                              console.log("/////////////////////////////////////////////////////////////////");
                              console.log("/////////////////////////////////////////////////////////////////");
                              // let { beerlist, venue_db_id } = data;
                              let { currentBeers, nextBeers, beerslistTotal, tickerInfo, userSettings } = data;
                              console.log(currentBeers);
                              console.log(tickerInfo);
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
          console.log(displayElement);
          if (displayElement != null) {
            console.log("IN THE DISPLAY ELEMENT");
            console.log(displayElement);
            displayElement = document.querySelector('#' + screenElementUserId + ' #beerlist');
            console.log(displayElement);
            screenDisplay = displayElement;
            console.log(screenDisplay);
          }

            let tickerTextEl = document.querySelector('#ticker-text');
            screenDisplay.innerHTML = '';
            currentBeers.forEach(beer => {
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
                          // console.log(beerlistData[i]);
                          option.value = beerlistData[i].id;
                          option.text = beerlistData[i].name;
                          selectNode.options[i] = new Option(beerlistData[i].name, i);
                          selectNode.options[i].value = beerlistData[i].id;
                          // console.log(selectNode.innerHTML);
                      }

                      // edit_beer_list add beer of the month checkbox
                      bomDivNode.classList.add("form-group");
                      bomCheckbox.id = `bom-beer_${beer.id_dropdown}`;
                      bomCheckbox.setAttribute("type", "checkbox");
                      bomCheckbox.setAttribute("name", `beer-of-month_${beer.id_dropdown}`);
                      console.log(`beer.beer_of_month = ${beer.beer_of_month}`);
                      if (beer.beer_of_month == true) {
                        bomCheckbox.setAttribute("value", beer.beer_of_month);

                      } else {
                        bomCheckbox.setAttribute("value", beer.beer_of_month);
                      }

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
                      comingSoonCheckbox.id = `comingSoon-beer_${beer.id_dropdown}`;
                      comingSoonCheckbox.setAttribute("type", "checkbox");
                      comingSoonCheckbox.setAttribute("name", `coming-soon_${beer.id_dropdown}`);
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
    // console.log(displayData);
    const { bottleBeerlist, userSettings } = displayData;
    let beersData = bottleBeerlist.beerlist;
    // console.log(beersData);

    let userId = userSettings.venue_db_id;

    if (Object.getOwnPropertyNames(userId).length >= 1) {

        // console.log(userId);
        let screenElementUserId = 'user-id-' + userId;
        // console.log(screenElementUserId);
        let displayListElement = document.querySelector('#' + screenElementUserId + ' .beer-list-loop-bb');
        if (displayListElement != null) {
          // console.log(displayListElement);

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

}
