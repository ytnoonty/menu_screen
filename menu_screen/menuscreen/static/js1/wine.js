class Wine {
  constructor() {
    this.name = 'WINENAME';
    this.location = 'WINELOCATION';
    this.description = 'WINEDESCRIPTION';
    this.glass = 'WINEGLASS';
    this.bottle = 'WINEBOTTLE';
    this.varietal = 'WINEVARIETAL';
  }

  async getWineList() {
    const dbResponse = await fetch('/_getwines');
    const results = await dbResponse.json();
    console.log(results);
    return {
      results: results
    }
  }
  async getCurrentWinelist() {
    const dbResponse = await fetch('/_getCurrentWinelist');
    const results = await dbResponse.json();
    return {
      results: results
    }
  }
}
