class ScreenUpdater {
  async screenUpdate() {
    const dbResponse = await fetch('/_screen_display');
    const result = await dbResponse.json();
    return {
      result: result
    }
  }
  fetchScreenUpdate() {
    fetch('/_screen_display')
    .then((res) => res.json())
    .then((data) => {
      return {
        data: data
      }
    })
  }
  // fetchScreenUpdate() {
  //   const dbResponse = fetch('/_screen_display');
  //   const result = dbResponse.json();
  //   return {
  //     result: result
  //   }
  // }
}
