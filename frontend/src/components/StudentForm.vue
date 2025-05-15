<template>
  <div class="container">
    <h2 class="title">学生请假申请</h2>
    <form @submit.prevent="submitLeaveRequest" class="form">
      <div class="form-group">
        <label for="studentName">姓名:</label>
        <input
          v-model="studentName"
          type="text"
          id="studentName"
          required
          class="form-control"
        />
      </div>
      <div class="form-group">
        <label for="leaveReason">请假原因:</label>
        <textarea
          v-model="leaveReason"
          id="leaveReason"
          required
          class="form-control"
        ></textarea>
      </div>
      <div class="form-group">
        <label for="leaveDate">申请日期:</label>
        <input
          v-model="leaveDate"
          type="date"
          id="leaveDate"
          required
          class="form-control"
        />
      </div>
      <div class="form-group">
        <label for="returnDate">返校日期:</label>
        <input
          v-model="returnDate"
          type="date"
          id="returnDate"
          required
          class="form-control"
        />
      </div>
      <div v-if="dateError" class="error-message">
        请假日期必须早于或等于返校日期！
      </div>
      <button type="submit" :disabled="isSubmitting || dateError" class="btn btn-primary">
        提交申请
      </button>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      studentName: '',
      leaveReason: '',
      leaveDate: '',
      returnDate: '',
      dateError: false,
      isSubmitting: false,
      leaveRequests: []
    };
  },
  methods: {
    submitLeaveRequest() {
      if (this.leaveDate > this.returnDate) {
        this.dateError = true;
        return;
      }

      this.dateError = false;
      this.isSubmitting = true;

      const newRequest = {
        studentName: this.studentName,
        leaveReason: this.leaveReason,
        leaveDate: this.leaveDate,
        returnDate: this.returnDate,
        status: 'pending'
      };

      this.leaveRequests.push(newRequest);

      this.studentName = '';
      this.leaveReason = '';
      this.leaveDate = '';
      this.returnDate = '';

      alert('请假申请已提交！');
      this.isSubmitting = false;

      console.log('Mock 数据:', this.leaveRequests);
    }
  }
};
</script>

<style scoped>
.container {
  max-width: 600px;
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

.form {
  display: flex;
  flex-direction: column;
}

.form-group {
  margin-bottom: 15px;
}

.form-group label {
  display: block;
  margin-bottom: 5px;
  color: #555;
}

.form-control {
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-sizing: border-box;
}

.form-control:focus {
  border-color: #007bff;
  outline: none;
}

.error-message {
  color: red;
  margin-bottom: 10px;
}

.btn {
  padding: 10px 20px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 16px;
  transition: background-color 0.3s;
}

.btn-primary {
  background-color: #007bff;
  color: white;
}

.btn-primary:hover {
  background-color: #0056b3;
}

.btn:disabled {
  background-color: #ccc;
  cursor: not-allowed;
}
</style>