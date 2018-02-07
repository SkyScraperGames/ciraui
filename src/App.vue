<template>
  <div id="app">
    <navbar></navbar>
    <main id="content">
      <router-view></router-view>
    </main>
    <cira-footer></cira-footer>
  </div>
</template>

<script>
  import Footer from './components/partials/Footer';
  import Navbar from './components/partials/Navbar';

  export default {
    name: 'app',
    components: {
      'cira-footer': Footer,
      Navbar,
    },
  };
</script>

<style lang="scss">
  @import "./styles/_variables";
  @import "./styles/utilities";

  html, body {
    overflow: hidden !important;
    height: 100vh;
  }

  #app {
    display: flex;
    flex-direction: column;
    height: 100vh;
    overflow-y: scroll;

    #content {
      flex: 1;
    }
  }
</style>
