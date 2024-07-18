import { createStore } from 'vuex'

export default createStore({
  state: {
    customer: {
      customername: ''
    }
  },
  getters: {
    isAuthenticated(state) {
      return !!state.customer.customername;
    }
  },
  mutations: {
    setCustomer(state, customername) {
      state.customer.customername = customername;
    },
    clearCustomer(state) {
      state.customer.customername = '';
    }
  },
  actions: {
    saveCustomer({ commit }, customername) {
      localStorage.setItem('customername', customername);
      commit('setCustomer', customername);
    },
    loadCustomer({ commit }) {
      const customername = localStorage.getItem('customername');
      if (customername) {
        commit('setCustomer', customername);
      }
    },
    clearCustomer({ commit }) {
      localStorage.removeItem('customername');
      commit('clearCustomer');
    }
  },
  modules: {
  }
});


