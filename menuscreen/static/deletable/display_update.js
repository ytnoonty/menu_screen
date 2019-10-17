class ScreenUpdater {
  async function screenUpdate() {
    const dbResponse = await fetch('/_screen_display');
    const result = await dbResponse.json();
    console.log('THIS IS THE RESULT');
    console.log(result);
    return {
      result: result
    }
  }
}
