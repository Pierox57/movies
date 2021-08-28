<template>
  <div class="movies-detail">
    <div class="flex justify-center">
      <h2 class="flex-initial">{{ movie.title }}</h2>
      <router-link :to="{ name: 'MoviesEdit', params: { id: this.$route.params.id } }" class="flex-initial inline-block bg-blue-500 text-white rounded p-1 mx-2 mb-8 mt-1">Edit</router-link>
    </div>
    <div class="container mx-auto w-1/2">
      <h3>Description</h3>
      <p class="text-justify">{{ movie.description }}</p>
      <h3>Actors</h3>
      <ul>
        <li v-for="actor in movie.actors" :key="actor">
          - {{ actor.first_name }} {{ actor.last_name }}
        </li>
      </ul>
      <div class="flex">
        <h3 class="flex-initial">Grade</h3>
        <router-link :to="{ name: 'ReviewsAdd', params: { id: this.$route.params.id } }" class="flex-initial inline-block bg-blue-500 text-white rounded px-1 mx-2 mb-6 mt-1">Add</router-link>
      </div>
      <p>{{ average }} / 5</p>
    </div>
  </div>
</template>

<script>
import { mapState, mapActions, mapGetters } from "vuex";

export default {
  name: "MoviesDetail",
  data() {
    return {
      average: Number,
    };
  },
  computed: {
    ...mapState(["movie", "error"]),
    ...mapGetters(["reviewAverage"]),
  },
  methods: {
    ...mapActions(["getMovie"]),
  },
  mounted() {
    this.getMovie(this.$route.params.id)
      .then(() => {
        this.average = this.reviewAverage;
      })
      .catch(() => {
        console.error(this.error);
      });
  },
};
</script>
