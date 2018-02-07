<template>
  <div>
    <div class="container">
      <h1 class="is-size-1 mb-20">Code Editor</h1>
    </div>
    <editor :code="code" :name="name" :loaded="this.$route.params.id !== undefined"></editor>
  </div>
</template>

<script>
  import { load } from '../../api/editor';
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
    mounted() {
      const vm = this;

      if (this.$route.params.id !== undefined) {
        load(this.$route.params.id)
          .then((response) => {
            if (!response.ok) {
              return;
            }

            response.json().then((data) => {
              vm.code = data.pycode;
              vm.name = data.title;
            });
          });
      }
    },
  };
</script>
