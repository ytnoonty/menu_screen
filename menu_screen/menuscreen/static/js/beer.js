class Beer {
  constructor() {
    this.name = 'BEERNAME';
    this.style = 'BEERSTYLE';
    this.abv = 'BEERABV';
    this.ibu = 'BEERIBU';
    this.brewery = 'BEERBREWERY';
    this.location = 'BEERLOCATION';
    this.website = 'BEERWEBSITE';
    this.description = 'BEERDESCRIPTION';
    this.draftBottle = 'BEERDRAFTBOTTLE';
  }

  async getBeer(name) {
    const dbResponse = await fetch(`/_searchBeerlist/${name}/`);
    const result = await dbResponse.json();
    return {
      result: result
    }
  }
  async getBeerList() {
    const dbResponse = await fetch('/_updateBeersDashboard');
    const results = await dbResponse.json();
    return {
      results: results
    }
  }
  async getBeelistSettings() {
    const dbResponse = await fetch('/_screen_display');
    const results = await dbResponse.json();
    return {
      results: results
    }
  }
}
