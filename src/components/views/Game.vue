<template>
  <editor :code="code" :name="name" loaded="true"></editor>
</template>

<script>
  import Editor from '../partials/Editor';

  export default {
    data() {
      return {
        code: '',
        name: '',
      };
    },
    components: {
      Editor,
    },
    watch: {
      /* eslint-disable */
      '$route.params.game': function (game) {
        this.loadGame(game);
      },
    },
    mounted() {
      this.loadGame(this.$route.params.game);
    },
    methods: {
      loadGame(game) {
        import(`../../assets/python/games/${game}.py`)
          .then((file) => {
            this.code = file;
            this.name = `${game}.py`;
          });
      },
    },
  };
</script>
