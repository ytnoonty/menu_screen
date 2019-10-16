class ScreenUpdater {
  async screenUpdate() {
    const dbResponse = await fetch('/_screen_display');
    const result = await dbResponse.json();
    return {
      result: result
    }
  }
}
