<script>
  let data;
  let val;
  let ph;
  let hardness;
  let solids;
  let Chloramines;
  let sulphate;
  let Conductivity;
  let organic_carbon;
  let trihalomethanes;
  let turbidity;
  let potability;
  async function getData(){
    potability = undefined;
    console.log(val)
    data  = await fetch("http://localhost:6969/water/" + ph + '/' +hardness + '/' + solids + '/' + Chloramines + '/' + sulphate + '/' + Conductivity + '/' + organic_carbon + '/' + turbidity + '/' + trihalomethanes );
    potability = Number(await data.text());
  }

  $: o = (potability ? "Water is safe to drink" : "Water is unsafe to drink");

</script>

<main>
  <h1 class="title">  
  Water Potability Calculator
  </h1>
  <div class='container'>
    <div class="pane">

      <div class="inputGroup">
        <div class='inputLabel'>pH</div>
        <input bind:value={ph} class="inputBox"/>
      </div>

      <div class="inputGroup">
        <div class='inputLabel'>Hardness</div>
        <input bind:value={hardness} class="inputBox"/>
      </div>

      <div class="inputGroup">
        <div class='inputLabel'>Solids</div>
        <input bind:value={solids} class="inputBox" />
      </div>

      <div class="inputGroup">
        <div class='inputLabel'>Chloramines</div>
        <input bind:value={Chloramines} class="inputBox"/>
      </div>

      <div class="inputGroup">
        <div class='inputLabel'>Sulphate</div>
        <input bind:value={sulphate} class="inputBox"/>
      </div>

    </div>
    <div class="pane">
      <div class="inputGroup">
        <div class='inputLabel'>Conductivity</div>
        <input bind:value={Conductivity} class="inputBox"/>
      </div>
      <div class="inputGroup">
        <div class='inputLabel'>Organic Carbon</div>
        <input bind:value={organic_carbon} class="inputBox"/>
      </div>
      <div class="inputGroup">
        <div class='inputLabel'>Turbidity</div>
        <input bind:value={turbidity} class="inputBox"/>
      </div>
      <div class="inputGroup">
        <div class='inputLabel'>Trihalomethanes</div>
        <input bind:value={trihalomethanes} class="inputBox"/>
      </div>
      <div class=""></div>
      <button class="inputBox submitButton" on:click={getData}>Submit</button> 
    </div>
  </div>  
  <div class="inputLabel output">
    {#if data}
    {o}
    {/if}
  </div>
  
</main>

<style>
@import url('https://fonts.googleapis.com/css2?family=Sunflower:wght@700&display=swap');
.container{
    display: flex;
    flex-direction: row;
    gap: 5em;
  }
  .pane{
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    gap: 2em;
  }

  .inputLabel{
    font-family: 'Sunflower', sans-serif;
    font-size: 1.3em;
    color: #DFF6FF;
  }

  .inputGroup{
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    gap: 0.2em;
  }

  .inputBox{
    border-width: 0.2em;
    border-style: solid;
    border-color: #06283D;
    border-radius: 0.7em;
    background-color: #256D85;
    color: #DFF6FF;
    font-family: 'Sunflower', sans-serif;
    font-size: 120%;
    width: 70%;
    padding: 0.2em;
  }

  .submitButton{
    width: 74%;
    
  }

  .submitButton:hover{
   background-color: #06283D;
  }

  .title{
    color: #DFF6FF;
    font-family: 'Sunflower', sans-serif;
    margin-bottom: 1.5em;
  } 

  .output{
    margin: 3em;
  }

</style>
