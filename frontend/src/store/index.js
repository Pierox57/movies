import { createStore } from "vuex";
import axios from "axios";

var base_url = "http://127.0.0.1:8080";

export default createStore({
  state: {
    movies: [],
    page: 1,
    previous: false,
    next: false,
  },
  getters: {
    getNextPage: (state) => {
      return state.page + 1;
    },
    getPreviousPage: (state) => {
      return state.page - 1;
    },
  },
  mutations: {
    SET_TASKS(state, movies) {
      state.movies = movies;
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
        commit("SET_TASKS", response.data.results);
        commit("SET_PAGE", page);
        commit("SET_PREVIOUS", response.data.previous);
        commit("SET_NEXT", response.data.next);
      } catch (error) {
        commit("SET_ERROR", error);
        throw error;
      }
    },
  },
  modules: {},
});
