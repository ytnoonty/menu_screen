class Untappd {
  constructor() {
    this.client_id = '73213F326CBF3CC907ECF67E172BC4352CABE0A8';
    this.client_secret = '040AF1B573EF5BC56426E59D949A6AA086311C6F';

    this.beer = {
      'id': '',
      'name': '',
      'style': '',
      'abv': '',
      'ibu': '',
      'brewery': '',
      'location': '',
      'website': '',
      'description': '',
      'draftbottleselection': ''
    }
  }

  async getBeerByName(beer) {
    const untappdResponse = await fetch(`https://api.untappd.com/v4/search/beer?q=${beer}&client_id=${this.client_id}&client_secret=${this.client_secret}`);
    const results = await untappdResponse.json();
    return {
      results: results
    }
  }
  async getBeerById(beer) {
    const untappdResponse = await fetch(`https://api.untappd.com/v4/beer/info/${beer}?&compact=true&client_id=${this.client_id}&client_secret=${this.client_secret}`);
    const singleResult = await untappdResponse.json();
    return {
      singleResult: singleResult
    }
  }
}
