<template>
  <div class="container">
    <h1 class="is-size-1 mb-20">Help</h1>
    <div class="columns is-desktop is-multiline is-8">
      <router-link class="column is-one-quarter" to="/help/booleans">
        <div class="is-primary has-text-centered">
          <h2 class="is-size-3">Booleans</h2>
        </div>
      </router-link>
      <router-link class="column is-one-quarter" to="/help/conditionals">
        <div class="is-primary has-text-centered">
          <h2 class="is-size-3">Conditionals</h2>
        </div>
      </router-link>
      <router-link class="column is-one-quarter" to="/help/whitespace">
        <div class="is-primary has-text-centered">
          <h2 class="is-size-3">Whitespace</h2>
        </div>
      </router-link>
      <router-link class="column is-one-quarter" to="/help/loops">
        <div class="is-primary has-text-centered">
          <h2 class="is-size-3">Loops</h2>
        </div>
      </router-link>
      <router-link class="column is-one-quarter" to="/help/RGBColor">
        <div class="is-primary has-text-centered">
          <h2 class="is-size-3">RGB Color</h2>
        </div>
      </router-link>
      <router-link class="column is-one-quarter" to="/help/pixels">
        <div class="is-primary has-text-centered">
          <h2 class="is-size-3">Pixels</h2>
        </div>
      </router-link>
      <router-link class="column is-one-quarter" to="/help/displayGrid">
        <div class="is-primary has-text-centered">
          <h2 class="is-size-3">Display Grid</h2>
        </div>
      </router-link>
    </div>
  </div>
</template>

<style lang="scss" scoped>
  .is-primary {
    background-color: #00d1b2;
    color: #FFF;
    padding: 20px;
    border-radius: 5px;
  }
</style>
