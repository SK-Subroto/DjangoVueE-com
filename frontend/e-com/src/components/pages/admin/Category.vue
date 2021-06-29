<template>
  <div>
    <modal modalHeading="Add New Category" :cond="showingAddModal" @modalClose="showingAddModal=false">
      <table>
        <tr>
          <td>
            Category Name
          </td>
          <td>
            <input type="text" id="newCatName" v-model="newCategory.name" placeholder="Category Name">
          </td>
        </tr>

        <tr>
          <td>
            Category Description
          </td>
          <td>
            <textarea  id="" cols="30" rows="10" v-model="newCategory.description" placeholder="write short des..."></textarea>
          </td>
        </tr>

        <tr>
          <td>
            
          </td>
          <td>
            <button class="btnSave" @click="addNewCategory()">Save</button>
          </td>
        </tr>
      </table>
    </modal>

    <modal modalHeading="Update This Category" :cond="showingEditModal" @modalClose="showingEditModal=false">
      <table>
        <tr>
          <td>
            Category Name
          </td>
          <td>
            <input type="text" id="newCatName" v-model="clickCategory.name" placeholder="Category Name">
          </td>
        </tr>

        <tr>
          <td>
            Category Description
          </td>
          <td>
            <textarea  id="" cols="30" rows="10" v-model="clickCategory.description" placeholder="write short des..."></textarea>
          </td>
        </tr>

        <tr>
          <td>
            
          </td>
          <td>
            <button class="btnSave" @click="updateCategory()">Update</button>
          </td>
        </tr>
      </table>
    </modal>

    <modal modalHeading="Are you sure?" :cond="showingDeleteModal" @modalClose="showingDeleteModal=false">
      
      <h2>
        You are going to delete the category <b>{{ clickCategory.name }}</b>
      </h2>
      <table>
        <tr>
          <td>
            <button class="btnSave" @click="deleteCategory()">Yes</button>
          </td>
          <td>
            <button class="btnClose" @click="showingDeleteModal=false">No</button>
          </td>
        </tr>
      </table>
    </modal>

    <h2 class="fleft">Categories</h2>
    <button class="addBtn fright" @click="showingAddModal=true">Add New</button>
    <div class="clear"></div>
    <hr>

    <table class="nice-table">
      <tr>
        <th>ID</th>
        <th>Name</th>
        <th>Description</th>
        <th>Edit</th>
        <th>Delete</th>
      </tr>

      <tr v-for="(category, i) in categories" :key="i">
        <td>{{ category.id }}</td>
        <td>{{ category.name }}</td>
        <td>{{ category.description }}</td>
        <td><button class="edit" @click="showingEditModal = true; clickCategory = category">Edit</button></td>
        <td><button class="delete" @click="showingDeleteModal = true; clickCategory = category">Delete</button></td>
      </tr>
    </table>
  </div>
</template>

<script>
export default {
  name: 'Category',
  data () {
    return {
      showingAddModal: false,
      showingEditModal: false,
      showingDeleteModal: false,

      newCategory:{
        name: "",
        description: ""
      },
      clickCategory: {},
      categories: []
    }
  },
  mounted(){
    this.init();
  },
  updated(){
    console.log(new Date())
  },
  watch: {
    'newCategory.name': function(){
      console.log(this.newCategory.name)
    }
  },
  methods: {
      init(){
        this.$eventBus.$emit("loadingStatus", true);

        this.$axios.get("http://localhost:8000/api/category")
          .then(res=> {
            this.$eventBus.$emit("loadingStatus", false);
            this.categories = res.data
          })
      },

      addNewCategory(){

        if(!this.newCategory.name){
          
          this.$iziToast.error({
              title: 'Error',
              message: "Category name can't be empty!" 
            })

            var catNameInput = document.getElementById("newCatName");
            catNameInput.focus();
          return;
        }

        this.$eventBus.$emit("loadingStatus", true);
        this.$axios.post("http://localhost:8000/api/category/create", this.newCategory)
          .then(res => {
              this.$eventBus.$emit("loadingStatus", false)
              this.showingAddModal = false
              // console.log(res.data);
              // localStorage.setItem("token", res.data["jwt"])
              this.init()
                this.$iziToast.success({
                  title: 'Success',
                  message: res.data.message
                })
          })
          .catch(err => {
            // alert(err.response.data["detail"])
            this.$eventBus.$emit("loadingStatus", false)
            this.showingAddModal = false
            this.$iziToast.error({
              title: 'Error',
              message: err.response.data.error 
            })
          })
      },

      updateCategory(){
        console.log(this.clickCategory.id)
        this.$eventBus.$emit("loadingStatus", true);
        this.$axios.put("http://localhost:8000/api/category/update/"+this.clickCategory.id, this.clickCategory)
          .then(res => {
              this.$eventBus.$emit("loadingStatus", false)
              this.showingEditModal = false
              this.init();
                this.$iziToast.success({
                  title: 'Success',
                  message: res.data.message
                })
          })
          .catch(err => {
            // alert(err.response.data["detail"])
            this.$eventBus.$emit("loadingStatus", false)
            this.showingAddModal = false
            this.$iziToast.error({
              title: 'Error',
              message: err.response.data.error 
            })
          })

          this.clickCategory = {};
          console.log("done")
      },

      deleteCategory() {
        this.$eventBus.$emit("loadingStatus", true);
        this.$axios.delete("http://localhost:8000/api/category/delete/"+this.clickCategory.id, this.clickCategory)
          .then(res => {
              this.$eventBus.$emit("loadingStatus", false)
              this.init();
              this.showingDeleteModal = false
                this.$iziToast.success({
                  title: 'Success',
                  message: res.data.message
                })
          })
          .catch(err => {
            // alert(err.response.data["detail"])
            this.$eventBus.$emit("loadingStatus", false)
            this.showingAddModal = false
            this.$iziToast.error({
              title: 'Error',
              message: err.response.data.error 
            })
          })

          this.clickCategory = {};
          
      }
  }
}
</script>
