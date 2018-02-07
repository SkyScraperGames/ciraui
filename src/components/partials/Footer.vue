<template>
  <footer class="cira-footer has-text-right" :class="{ home: isHome }">
    <div class="container">
      &copy; Skyscraper Games 2018. All Rights Reserved.
      <router-link to="/privacy">Privacy Policy</router-link>
    </div>
  </footer>
</template>

<style lang="scss" scoped>
  .cira-footer {
    padding: 20px 0;
    box-sizing: border-box;

    a {
      text-decoration: underline;
    }

    &.home {
      position: absolute;
      bottom: 0;
      left: 0;
      right: 0;
      color: #FFF;

      a {
        color: #FFF;
      }
    }
  }
</style>

<script>
export default {
  computed: {
    isHome() {
      return this.$route.path === '/';
    },
  },
};
</script>

