<template>
  <div class="container">
    <h1 class="is-size-1 mb-20">Lessons</h1>
    <div class="columns is-desktop is-multiline is-8">
      <router-link class="column is-one-quarter" v-for="lesson in lessons" :key="lesson.directory" :to="`/lessons/${lesson.directory}`">
        <div class="is-primary has-text-centered">
          <h2 class="is-size-4">{{ lesson.name }}</h2>
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

<script>
  import lessons from '../../assets/lessons/lessons.json';

  export default {
    data() {
      return {
        lessons,
      };
    },
  };
</script>

