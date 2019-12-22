class WineTemplate {
  constructor() {
      this.updateScreenTemplates = () => {

      }
  }

  wineTabletTemplate(displayData) {
      console.log(displayData);
      const { wineTypelist, winelist, userData } = displayData;
      console.log(wineTypelist, winelist, userData);

      let userSettingsData = userData;
      let screenDisplay;
      let screenElementUserId = 'user-id-' + userSettingsData.venue_db_id;
      console.log(screenElementUserId);
      let displayElement = document.querySelector('#' + screenElementUserId);

      if (displayElement != null) {
        displayElement = document.querySelector('#' + screenElementUserId + ' #winelist-tablet-menu');
        console.log('************wineTabletTemplate*************');
        console.log(displayElement);
        console.log('************wineTabletTemplate*************');
      }

      let wineMenuHTML = '';
      wineTypelist.forEach(wineType => {
        console.log(wineType);
        wineMenuHTML += `
          <div class="row mt-0">
            <div class="row justify-content-center col-12 mx-auto">
              <div class="row justify-content-center col-12 border-bottom">
                <h1 class="mt-0 bold-font">${ wineType }</h1>
              </div>
            </div>
            <div id="winelist-menu-wines" class="row col-12 justify-content-center mx-auto">
            `;
              winelist.forEach(wine => {
                if (wine.type == wineType) {
                  wineMenuHTML+= `
                      <!-- BEGIN CARD -->
                      <div class="text-center" style="width: 100%;">
                        <div class="">
                          <div class="row mt-3">
                            <div class="col">
                              <div>
                                <h3 class="mb-0"><span class="card-title mb-1 larger-text txt-clr-grn"> ${wine.name} </span></h3>
                                <span class="card-text mb-1 italic-font bold-font font-sml"> ${wine.varietal} </span>
                                <span class="card-text mb-1 italic-font font-xsml">( ${wine.location} )</span>
                              </div>
                              <div class="font-xsml">Gls.....  <span> ${wine.glass} </span>
                              <span>Btl.....  </span><span> ${wine.bottle} </span></div>
                            </div>
                          </div>
                        </div>
                      </div>
                      <!-- END CARD -->
                  `;
                }
              });
            wineMenuHTML +=`
            </div>
          </div>
          `;
      });

      if (displayElement != null) {
        displayElement.innerHTML = wineMenuHTML;
      }
  }

  wineDescriptionsTabletTemplate (displayData) {
      // console.log("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&");
      // console.log("DESCRIBING WINES NOW");
      // console.log(displayData);
      // console.log("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&");

      const { wineTypelist, winelist, userData } = displayData;
      // console.log(wineTypelist, winelist, userData);

      let userSettingsData = userData;
      let screenDisplay;
      let screenElementUserId = 'user-id-' + userSettingsData.venue_db_id;
      // console.log(screenElementUserId);
      let displayElement = document.querySelector('#' + screenElementUserId);
      // console.log(displayElement);

      if (displayElement != null) {
        displayElement = document.querySelector('#' + screenElementUserId + ' #winelist-tablet-descriptions');
        // console.log('************wineTablet Description Template*************');
        // console.log(displayElement);
        // console.log('************wineTablet Description Template*************');
      }

      let wineDescriptionHTML = '';
      wineTypelist.forEach(wineType => {
        wineDescriptionHTML += `
          <div class="row mt-0">
            <div class="row justify-content-center col-12 mx-auto">
              <div class="row justify-content-center col-12 border-bottom">
                <h1 class="mt-0 bold-font text-center">${ wineType }</h1>
              </div>
            </div>
            <div id="winelist-menu-descriptions" class="row col-12 justify-content-center mx-auto">
            `;
              winelist.forEach(wine => {
                if (wine.type == wineType) {
                  wineDescriptionHTML += `
                      <!-- BEGIN CARD -->
                      <div class="text-center" style="width: 100%;">
                        <div class="">
                          <div class="row mt-3">
                            <div class="col">
                              <div>
                                <h3 class="mb-0"><span class="card-title mb-1 larger-text txt-clr-grn"> ${wine.name} </span></h3>
                                <span class="card-text mb-1 italic-font bold-font font-sml"> ${wine.varietal} </span>
                                <span class="card-text mb-1 italic-font font-xsml">( ${wine.location} )</span>
                              </div>
                              <div>
                                <span class="font-med">Description: </span><span> ${wine.description} </span>
                              </div>
                              <div>
                                <span class="font-med">Pairs with: </span><span> ${wine.foodPairings} </span>
                              </div>
                            </div>
                          </div>
                        </div>
                      </div>
                      <!-- END CARD -->
                  `;
                }
              });
            wineDescriptionHTML +=`
            </div>
          </div>
          `;
      });
      if (displayElement != null) {
        displayElement.innerHTML = wineDescriptionHTML;
      }
  }


}
