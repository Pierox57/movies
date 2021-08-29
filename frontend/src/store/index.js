import { createStore } from "vuex";
import axios from "axios";

const base_url = "http://127.0.0.1:8080";

export default createStore({
  state: {
    movies: [],
    movie: [],
    actors: [],
    page: 1,
    previous: false,
    next: false,
    error: null,
  },
  getters: {
    getNextPage: (state) => {
      return state.page + 1;
    },
    getPreviousPage: (state) => {
      return state.page - 1;
    },
    reviewAverage: (state) => {
      var sum = 0;
      state.movie.reviews.forEach((review) => {
        sum += review.grade;
      });
      return (sum / state.movie.reviews.length).toFixed(1);
    },
  },
  mutations: {
    SET_MOVIES(state, movies) {
      state.movies = movies;
    },
    SET_MOVIE(state, movie) {
      state.movie = movie;
    },
    SET_ACTORS(state, actors) {
      state.actors = actors;
    },
    SET_PAGE(state, page) {
      state.page = page;
    },
    SET_NEXT(state, next) {
      if (next) state.next = true;
      else state.next = false;
    },
    SET_PREVIOUS(state, previous) {
      if (previous) state.previous = true;
      else state.previous = false;
    },
    SET_ERROR(state, error) {
      state.error = error;
    },
  },
  actions: {
    async getMovies({ commit }, page) {
      try {
        const response = await axios.get(base_url + "/movies/", {
          params: {
            format: "json",
            page: page,
          },
        });
        commit("SET_MOVIES", response.data.results);
        commit("SET_PAGE", page);
        commit("SET_PREVIOUS", response.data.previous);
        commit("SET_NEXT", response.data.next);
      } catch (error) {
        commit("SET_ERROR", error);
        throw error;
      }
    },
    async getMovie({ commit }, id) {
      try {
        const response = await axios.get(base_url + "/movies/" + id + "/", {
          params: {
            format: "json",
          },
        });
        commit("SET_MOVIE", response.data);
      } catch (error) {
        commit("SET_ERROR", error);
        throw error;
      }
    },
    async updateMovie({ commit }, movie) {
      try {
        const response = await axios.put(
          base_url + "/movies/" + movie.id + "/",
          {
            title: movie.title,
            description: movie.description,
            actors: movie.actors,
            reviews: movie.reviews,
            params: {
              format: "json",
            },
          }
        );
        commit("SET_MOVIE", response.data);
      } catch (error) {
        commit("SET_ERROR", error);
        throw error;
      }
    },
    async getActors({ commit }) {
      try {
        const response = await axios.get(base_url + "/actors/", {
          params: {
            format: "json",
          },
        });
        commit("SET_ACTORS", response.data);
      } catch (error) {
        commit("SET_ERROR", error);
        throw error;
      }
    },
    async createReview({ commit }, review) {
      try {
        await axios.post(base_url + "/reviews/", {
          grade: review.grade,
          movie: review.movie,
          params: {
            format: "json",
          },
        });
      } catch (error) {
        commit("SET_ERROR", error);
        throw error;
      }
    },
  },
  modules: {},
});
