<template>
  <div class="container">
    <h1 class="is-size-1 mb-20">{{ lessonGroup.name }} Lessons</h1>
    <div class="columns is-desktop is-multiline is-8">
      <router-link class="column is-one-quarter" v-for="lesson in lessonGroup.lessons" :key="lesson.directory" :to="`/lessons/${lessonGroup.directory}/${lesson.directory}`">
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
    computed: {
      lessonGroup() {
        let lessonGroup;

        lessons.forEach((lesson) => {
          if (lesson.directory === this.$route.params.lessonGroup) lessonGroup = lesson;
        });

        return lessonGroup;
      },
    },
  };
</script>

