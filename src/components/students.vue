<template>
  <div>
    <h2>学生请假申请</h2>
    <form @submit.prevent="submitLeaveRequest">
      <label>
        姓名:
        <input v-model="studentName" type="text" required>
      </label>
      <br>
      <label>
        请假原因:
        <textarea v-model="leaveReason" required></textarea>
      </label>
      <br>
      <label>
        申请日期:
        <input v-model="leaveDate" type="date" required>
      </label>
      <br>
      <label>
        返校日期:
        <input v-model="returnDate" type="date" required>
      </label>
      <br>
      <div v-if="dateError" class="error-message">
        请假日期必须早于或等于返校日期！
      </div>
      <button type="submit" :disabled="isSubmitting || dateError">提交申请</button>
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
      isSubmitting: false
    };
  },
  methods: {
    async submitLeaveRequest() {
      if (this.leaveDate > this.returnDate) {
        this.dateError = true;
        return;
      }

      this.dateError = false;
      this.isSubmitting = true;

      try {
        const response = await this.$axios.post('/api/submit-leave', {
          studentName: this.studentName,
          leaveReason: this.leaveReason,
          leaveDate: this.leaveDate,
          returnDate: this.returnDate
        });
        alert('请假申请提交成功！');
        this.studentName = '';
        this.leaveReason = '';
        this.leaveDate = '';
        this.returnDate = '';
      } catch (error) {
        alert('提交失败，请稍后再试。');
      } finally {
        this.isSubmitting = false;
      }
    }
  }
};
</script>

<style scoped>
.error-message {
  color: red;
  margin-bottom: 10px;
}
</style>