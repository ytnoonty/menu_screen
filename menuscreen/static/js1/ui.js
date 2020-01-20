class UI {
  constructor() {
    this.searchresults = document.getElementById('searchresults');
    this.wineList = document.getElementById('wine-list');
    this.winelistMenu = document.getElementById('winelist-menu');
  }

  // Show profile in ui
  showBeerList(beer) {
    let output = '';
    output += `
      <table class="table table-striped">
        <tr>
          <th>Beer Id</th>
          <th>Name</th>
          <th>Style</th>
          <th>ABV</th>
          <th>IBU</th>
          <th>Brewery</th>
          <th>Location</th>
          <th>Website</th>
          <th>Description</th>
          <th></th>
          <th></th>
        </tr>`;
      beer.response.beers.items.forEach(function(beer) {
        output += `
          <tr class="beer-tr">
            <td>${beer.beer.bid}</td>
            <td>${beer.beer.beer_name}</span></td>
            <td>${beer.beer.beer_style}</td>
            <td>${beer.beer.beer_abv}</td>
            <td>${beer.beer.beer_ibu}</td>
            <td>${beer.brewery.brewery_name}</td>
            <td>${beer.brewery.location.brewery_city}, ${beer.brewery.location.brewery_state} - ${beer.brewery.country_name}</td>
            <td>${beer.brewery.contact.url}</td>
            <td>${beer.beer.beer_description}</td>
            <td></td>
            <td></td>
          </tr>
        `;
      });
    output += `
      </table>
      `;
    this.searchresults.innerHTML = output;
  }

  showBeerCandidate(beer) {
    let selectedBeer = beer.response.beer;
    let output = '';
    output += `
      <table class="table table-striped">
        <tr>
          <th>Beer Id</th>
          <th>Name</th>
          <th>Style</th>
          <th>ABV</th>
          <th>IBU</th>
          <th>Brewery</th>
          <th>Location</th>
          <th>Website</th>
          <th>Description</th>
          <th>Draft/Bottle</th>
          <th></th>
          <th></th>
        </tr>`;
    output += `
        <tr>
          <td id="beer_id">${selectedBeer.bid}</td>
          <td id="beer_name">${selectedBeer.beer_name}</td>
          <td id="beer_style">${selectedBeer.beer_style}</td>
          <td id="beer_abv">${selectedBeer.beer_abv}</td>
          <td id="beer_ibu">${selectedBeer.beer_ibu}</td>
          <td id="brewery_name">${selectedBeer.brewery.brewery_name}</td>
          <td id="brewery_location">${selectedBeer.brewery.location.brewery_city}, ${selectedBeer.brewery.location.brewery_state}, ${selectedBeer.brewery.country_name}</td>
          <td id="brewery_url">${selectedBeer.brewery.contact.url}</td>
          <td id="beer_description">${selectedBeer.beer_description}</td>
          <td>
            <div>
              <input class="bottle-draft" type="radio" id="draft"
                     name="beer" value="Draft" checked="true" />
              <label for="draft">Draft</label>
            </div>
            <div>
                <input class="bottle-draft" type="radio" id="bottle"
                       name="beer" value="Bottle" />
                <label for="bottle">Bottle</label>
            </div>
            <div>
                <input class="bottle-draft" type="radio" id="can"
                       name="beer" value="Can" />
                <label for="can">Can</label>
            </div>
            <div>
                <input class="bottle-draft" type="radio" id="draftBottle"
                       name="beer" value="Draft & Bottle" />
                <label for="draftBottle">Draft & Bottle</label>
            </div>
            <div>
                <input class="bottle-draft" type="radio" id="draftCan"
                       name="beer" value="Draft & Can" />
                <label for="draftCan">Draft & Can</label>
            </div>
            <div>
                <input class="bottle-draft" type="radio" id="bottleCan"
                       name="beer" value="Bottle & Can" />
                <label for="bottleCan">Bottle & Can</label>
            </div>
            <div>
                <input class="bottle-draft" type="radio" id="draftBottleCan"
                       name="beer" value="Draft, Bottle & Can" />
                <label for="draftBottleCan">Draft, Bottle & Can</label>
            </div>

          </td>
          <td><a href="#" class="btn btn-success add-beer-to-db" type="">Add Beer</a></td>
          <td><a href="#" class="btn btn-danger btn-cancel">Cancel</a></td>
        </tr>
    `;
    output += `
      </table>
      `;
    this.searchresults.innerHTML = output;
  }

  showAddedBeer(beer) {
    let selectedBeer = JSON.parse(beer);
    // console.log(selectedBeer);
    let output = '';
    output += `
      <table class="table table-striped">
        <tr>
          <th>Beer Id</th>
          <th>Name</th>
          <th>Style</th>
          <th>ABV</th>
          <th>IBU</th>
          <th>Brewery</th>
          <th>Location</th>
          <th>Website</th>
          <th>Description</th>
          <th>Draft/Bottle</th>
          <th></th>
          <th></th>
        </tr>`;
    output += `
        <tr>
          <td id="beer_id">${selectedBeer.id}</td>
          <td id="beer_name">${selectedBeer.name}</td>
          <td id="beer_style">${selectedBeer.style}</td>
          <td id="beer_abv">${selectedBeer.abv} %</td>
          <td id="beer_ibu">${selectedBeer.ibu}</td>
          <td id="brewery_name">${selectedBeer.brewery}</td>
          <td id="brewery_location">${selectedBeer.location}</td>
          <td id="brewery_url">${selectedBeer.website}</td>
          <td id="beer_description">${selectedBeer.description}</td>
          <td id="beer_draftBottle">${selectedBeer.draftbottleselection}</td>
        </tr>
    `;
    output += `
      </table>
      `;
    this.searchresults.innerHTML = output;
  }

  showDashWineList(wines) {
      let output = '';
      wines = JSON.parse(wines);
      // console.log(wines);
      wines.forEach((wine)=> {
        output +=
          `<tr scope="row">
            <td>${wine.name}</td>
            <td>${wine.varietal}</td>
            <td>${wine.location}</td>
            <td>${wine.glass}</td>
            <td>${wine.bottle}</td>
            <td>${wine.description}</td>
            <td><a href="edit_wine/${wine.id}" class="btn btn-default pull-right">Edit</a></td>
            <td>
              <form action="{url_for('delete_wine', id=${wine.id})}}" method="post">
                <input type="hidden" name="_method" value="DELETE">
                <input type="submit" value="Delete" class="btn btn-danger">
              </form>
            </td>
          </tr>`
        ;
      });
      this.wineList.innerHTML = output;
    }

    updateWinelist(wines) {
      let winelistRedwine = document.getElementById('winelist-menu-redwine');
      let winelistWhitewine = document.getElementById('winelist-menu-whitewine');
      let winelistBlushwine = document.getElementById('winelist-menu-blushwine');
      let winelistSparklingwine = document.getElementById('winelist-menu-sparklingwine');
      let winelistHousewine = document.getElementById('winelist-menu-housewine');
      let redWine = wines.slice(0,10);
      let whiteWine = wines.slice(10,18);
      let blushWine = wines.slice(18,20);
      let sparklingWine = wines.slice(20,22);
      let houseWine = wines.slice(22,29);
      let output = '';


      redWine.forEach((wine)=>{
        output +=
        `<!-- BEGIN CARD -->
        <div class="text-center" style="width: 100%;">
          <div class="">
            <div class="row mt-3">
              <div class="col">
                <div>
                  <h3 class="mb-0"><span class="card-title mb-1 larger-text txt-clr-grn">${wine.name}</span></h3>
                  <span class="card-text mb-1 italic-font bold-font font-sml">${wine.varietal}</span>
                  <span class="card-text mb-1 italic-font font-xsml">(${wine.location})</span>
                </div>
                <div class="font-xsml">Gls.....  <span> ${wine.glass}</span>
                <span>Btl.....  </span><span> ${wine.bottle}</span></div>
              </div>
            </div>
          </div>
        </div>
        <!-- END CARD -->
        `;
      });
      winelistRedwine.innerHTML = output;

      output = '';
      whiteWine.forEach((wine)=>{
        output +=
        `<!-- BEGIN CARD -->
        <div class="text-center" style="width: 100%;">
          <div class="">
            <div class="row mt-3">
              <div class="col">
                <div>
                  <h3 class="mb-0"><span class="card-title mb-1 larger-text txt-clr-grn">${wine.name}</span></h3>
                  <span class="card-text mb-1 italic-font bold-font font-sml">${wine.varietal}</span>
                  <span class="card-text mb-1 italic-font font-xsml">(${wine.location})</span>
                </div>
                <div class="font-xsml">Gls.....  <span> ${wine.glass}</span>
                <span>Btl.....  </span><span> ${wine.bottle}</span></div>
              </div>
            </div>
          </div>
        </div>
        <!-- END CARD -->
        `;
      });
      winelistWhitewine.innerHTML = output;

      output = '';
      blushWine.forEach((wine)=>{
        output +=
        `<!-- BEGIN CARD -->
        <div class="text-center" style="width: 100%;">
          <div class="">
            <div class="row mt-3">
              <div class="col">
                <div>
                  <h3 class="mb-0"><span class="card-title mb-1 larger-text txt-clr-grn">${wine.name}</span></h3>
                  <span class="card-text mb-1 italic-font bold-font font-sml">${wine.varietal}</span>
                  <span class="card-text mb-1 italic-font font-xsml">(${wine.location})</span>
                </div>
                <div class="font-xsml">Gls.....  <span> ${wine.glass}</span>
                <span>Btl.....  </span><span> ${wine.bottle}</span></div>
              </div>
            </div>
          </div>
        </div>
        <!-- END CARD -->
        `;
      });
      winelistBlushwine.innerHTML = output;

      output = '';
      sparklingWine.forEach((wine)=>{
        output +=
        `<!-- BEGIN CARD -->
        <div class="text-center" style="width: 100%;">
          <div class="">
            <div class="row mt-3">
              <div class="col">
                <div>
                  <h3 class="mb-0"><span class="card-title mb-1 larger-text txt-clr-grn">${wine.name}</span></h3>
                  <span class="card-text mb-1 italic-font bold-font font-sml">${wine.varietal}</span>
                  <span class="card-text mb-1 italic-font font-xsml">(${wine.location})</span>
                </div>
                <div class="font-xsml">
                <span>Split.....  </span><span> ${wine.bottle}</span></div>
              </div>
            </div>
          </div>
        </div>
        <!-- END CARD -->
        `;
      });
      winelistSparklingwine.innerHTML = output;

      output = '';
      houseWine.forEach((wine)=>{
        output +=
        `<!-- BEGIN CARD -->
        <div class="text-center" style="width: 100%;">
          <div class="">
            <div class="row mt-3">
              <div class="col">
                <div>
                  <h3 class="mb-0"><span class="card-title mb-1 larger-text txt-clr-grn">${wine.name}</span></h3>
                  <span class="card-text mb-1 italic-font bold-font font-sml">${wine.varietal}</span>
                  <span class="card-text mb-1 italic-font font-xsml">(${wine.location})</span>
                </div>
                <div class="font-xsml">Gls.....  <span> ${wine.glass}</span>
                </div>
              </div>
            </div>
          </div>
        </div>
        <!-- END CARD -->
        `;
      });
      winelistHousewine.innerHTML = output;
    } // END updateWinelist()

    updateWinelistDescription(wines) {
      let winelistRedwine = document.getElementById('winelist-description-redwine');
      let winelistWhitewine = document.getElementById('winelist-description-whitewine');
      let winelistBlushwine = document.getElementById('winelist-description-blushwine');
      let winelistSparklingwine = document.getElementById('winelist-description-sparklingwine');
      let winelistHousewine = document.getElementById('winelist-description-housewine');
      let redWine = wines.slice(0,10);
      let whiteWine = wines.slice(10,18);
      let blushWine = wines.slice(18,20);
      let sparklingWine = wines.slice(20,22);
      let houseWine = wines.slice(22,29);
      let output = '';


      redWine.forEach((wine)=>{
        output +=
        `<!-- BEGIN CARD -->
        <div class="text-center" style="width: 100%;">
          <div class="">
            <div class="row mt-3">
              <div class="col">
                <div>
                  <h3 class="mb-0"><span class="card-title mb-1 larger-text txt-clr-grn">${wine.name}</span></h3>
                  <span class="card-text mb-1 italic-font bold-font font-sml">${wine.varietal}</span>
                  <span class="card-text mb-1 italic-font font-xsml">(${wine.location})</span>
                </div>
                <div>
                  <span class="font-med">Description: </span> ${wine.description}
                </div>
                <div>
                  <span class="font-med">Pairs with: </span> ${wine.foodPairings}
                </div>
              </div>
            </div>
          </div>
        </div>
        <!-- END CARD -->
        `;
      });
      winelistRedwine.innerHTML = output;

      output = '';
      whiteWine.forEach((wine)=>{
        output +=
        `<!-- BEGIN CARD -->
        <div class="text-center" style="width: 100%;">
          <div class="">
            <div class="row mt-3">
              <div class="col">
                <div>
                  <h3 class="mb-0"><span class="card-title mb-1 larger-text txt-clr-grn">${wine.name}</span></h3>
                  <span class="card-text mb-1 italic-font bold-font font-sml">${wine.varietal}</span>
                  <span class="card-text mb-1 italic-font font-xsml">(${wine.location})</span>
                </div>
                <div>
                  <span class="font-med">Description: </span> ${wine.description}
                </div>
                <div>
                  <span class="font-med">Pairs with: </span> ${wine.foodPairings}
                </div>
              </div>
            </div>
          </div>
        </div>
        <!-- END CARD -->
        `;
      });
      winelistWhitewine.innerHTML = output;

      output = '';
      blushWine.forEach((wine)=>{
        output +=
        `<!-- BEGIN CARD -->
        <div class="text-center" style="width: 100%;">
          <div class="">
            <div class="row mt-3">
              <div class="col">
                <div>
                  <h3 class="mb-0"><span class="card-title mb-1 larger-text txt-clr-grn">${wine.name}</span></h3>
                  <span class="card-text mb-1 italic-font bold-font font-sml">${wine.varietal}</span>
                  <span class="card-text mb-1 italic-font font-xsml">(${wine.location})</span>
                </div>
                <div>
                  <span class="font-med">Description: </span> ${wine.description}
                </div>
                <div>
                  <span class="font-med">Pairs with: </span> ${wine.foodPairings}
                </div>
              </div>
            </div>
          </div>
        </div>
        <!-- END CARD -->
        `;
      });
      winelistBlushwine.innerHTML = output;

      output = '';
      sparklingWine.forEach((wine)=>{
        output +=
        `<!-- BEGIN CARD -->
        <div class="text-center" style="width: 100%;">
          <div class="">
            <div class="row mt-3">
              <div class="col">
                <div>
                  <h3 class="mb-0"><span class="card-title mb-1 larger-text txt-clr-grn">${wine.name}</span></h3>
                  <span class="card-text mb-1 italic-font bold-font font-sml">${wine.varietal}</span>
                  <span class="card-text mb-1 italic-font font-xsml">(${wine.location})</span>
                </div>
                <div>
                  <span class="font-med">Description: </span> ${wine.description}
                </div>
                <div>
                  <span class="font-med">Pairs with: </span> ${wine.foodPairings}
                </div>
              </div>
            </div>
          </div>
        </div>
        <!-- END CARD -->
        `;
      });
      winelistSparklingwine.innerHTML = output;

      output = '';
      houseWine.forEach((wine)=>{
        output +=
        `<!-- BEGIN CARD -->
        <div class="text-center" style="width: 100%;">
          <div class="">
            <div class="row mt-3">
              <div class="col">
                <div>
                  <h3 class="mb-0"><span class="card-title mb-1 larger-text txt-clr-grn">${wine.name}</span></h3>
                  <span class="card-text mb-1 italic-font bold-font font-sml">${wine.varietal}</span>
                  <span class="card-text mb-1 italic-font font-xsml">(${wine.location})</span>
                </div>
                <div>
                  <span class="font-med">Description: </span> ${wine.description}
                </div>
                <div>
                  <span class="font-med">Pairs with: </span> ${wine.foodPairings}
                </div>
              </div>
            </div>
          </div>
        </div>
        <!-- END CARD -->
        `;
      });
      winelistHousewine.innerHTML = output;
    } // END updateCurrentWinelistDescription()

  } // END UI class
