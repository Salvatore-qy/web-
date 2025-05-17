<template>
  <div class="container">
    <h2 class="title">教师审批</h2>
    <div v-for="request in leaveRequests" :key="request.id" class="request-item">
      <p><strong>学生姓名:</strong> {{ request.studentName }}</p>
      <p><strong>请假原因:</strong> {{ request.leaveReason }}</p>
      <p><strong>请假日期:</strong> {{ request.leaveDate }}</p>
      <p><strong>返校日期:</strong> {{ request.returnDate }}</p>
      <p><strong>状态:</strong> {{ request.status }}</p>
      <button @click="approveRequest(request.id)" class="btn btn-success">批准</button>
      <button @click="rejectRequest(request.id)" class="btn btn-danger">拒绝</button>
    </div>
  </div>
</template>

<script>
import { computed } from 'vue';
import { useStore } from 'vuex';

export default {
  setup() {
    const store = useStore();
    const leaveRequests = computed(() => store.getters.getLeaveRequests);

    const approveRequest = (requestId) => {
      const updatedRequest = leaveRequests.value.find(req => req.id === requestId);
      if (updatedRequest) {
        updatedRequest.status = 'approved';
        store.dispatch('updateLeaveRequest', updatedRequest);
      }
    };

    const rejectRequest = (requestId) => {
      const updatedRequest = leaveRequests.value.find(req => req.id === requestId);
      if (updatedRequest) {
        updatedRequest.status = 'rejected';
        store.dispatch('updateLeaveRequest', updatedRequest);
      }
    };

    return {
      leaveRequests,
      approveRequest,
      rejectRequest
    };
  }
};
</script>

<style scoped>
.container {
  max-width: 800px;
  margin: 50px auto;
  padding: 20px;
  background: #fff;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  border-radius: 8px;
}

.title {
  text-align: center;
  color: #333;
  margin-bottom: 20px;
}

.table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 20px;
}

.table th,
.table td {
  padding: 10px;
  border: 1px solid #ddd;
  text-align: left;
}

.table th {
  background-color: #f4f4f4;
}

.btn {
  padding: 5px 10px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 14px;
  margin-right: 5px;
}

.btn-success {
  background-color: #28a745;
  color: white;
}

.btn-danger {
  background-color: #dc3545;
  color: white;
}

.no-requests {
  text-align: center;
  color: #555;
  margin-top: 20px;
}
</style>