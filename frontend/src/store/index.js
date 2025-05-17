import { createStore } from 'vuex';

export default createStore({
  state: {
    leaveRequests: []
  },
  mutations: {
    ADD_LEAVE_REQUEST(state, leaveRequest) {
      state.leaveRequests.push(leaveRequest);
    },
    UPDATE_LEAVE_REQUEST(state, updatedRequest) {
      const index = state.leaveRequests.findIndex(req => req.id === updatedRequest.id);
      if (index !== -1) {
        state.leaveRequests[index] = updatedRequest;
      }
    }
  },
  actions: {
    addLeaveRequest({ commit }, leaveRequest) {
      commit('ADD_LEAVE_REQUEST', leaveRequest);
    },
    updateLeaveRequest({ commit }, updatedRequest) {
      commit('UPDATE_LEAVE_REQUEST', updatedRequest);
    }
  },
  getters: {
    getLeaveRequests: state => state.leaveRequests
  }
});