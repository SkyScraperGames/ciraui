<template>
  <div class="home-wrapper">
    <div class="container has-text-centered">
      <h1 class="is-size-1 has-text-white">Become a skyscraper game designer!</h1>
      <router-link :to="getStartedLink" class="button is-large is-primary mt-25">
        <span>Get started</span>
        <b-icon icon="chevron-right"></b-icon>
      </router-link>
    </div>
  </div>
</template>

<script>
  import { mapState } from 'vuex';

  export default {
    computed: {
      ...mapState([
        'user',
      ]),
      getStartedLink() {
        if (!this.user) {
          return '/user/login';
        }

        return '/user/profile';
      },
    },
  };
</script>

<style lang="scss">
  @import "../../styles/_variables";

  .home-wrapper {
    height: 100%;
    background: linear-gradient(rgba(0, 0, 0, .5), rgba(0, 0, 0, .5)), url('../../assets/SkyscraperTetris.png');
    background-repeat: no-repeat;
    background-size: cover;
    background-position: center;
    display: flex;
    align-items: center;
  }
</style>
