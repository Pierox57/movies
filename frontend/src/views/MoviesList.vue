<template>
  <div class="movies-list">
    <h2>Movies list</h2>
    <div class="container mx-auto w-1/2">
      <ul class="flex flex-col justify-center m-2">
        <Movie
          v-for="movie in movies"
          :key="movie"
          :id="movie.id"
          :title="movie.title"
        />
      </ul>
      <button v-if="previous" @click="getPreviousMovies" class="m-2">
        Previous
      </button>
      <button v-if="next" @click="getNextMovies" class="m-2">Next</button>
    </div>
  </div>
</template>

<script>
import Movie from "@/components/Movie.vue";
import { mapState, mapGetters, mapActions } from "vuex";

export default {
  name: "MoviesList",
  components: {
    Movie,
  },
  computed: {
    ...mapState(["movies", "page", "previous", "next"]),
    ...mapGetters(["getPreviousPage", "getNextPage"]),
  },
  methods: {
    ...mapActions(["getMovies"]),
    getNextMovies() {
      this.getMoviesList(this.getNextPage);
    },
    getPreviousMovies() {
      this.getMoviesList(this.getPreviousPage);
    },
    getMoviesList(page) {
      this.getMovies(page).catch(() => {
        console.error(this.error);
      });
    },
  },
  mounted() {
    this.getMoviesList(this.page);
  },
};
</script>
