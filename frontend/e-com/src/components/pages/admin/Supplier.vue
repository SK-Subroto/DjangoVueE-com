<template>
  <div>
    <modal modalHeading="Add New Supplier" :cond="showingAddModal" @modalClose="showingAddModal=false">
      <table>
        <tr>
          <td>
            Supplier Name
          </td>
          <td>
            <input type="text" id="newCatName" v-model="newSupplier.name" placeholder="Supplier Name">
          </td>
        </tr>

        <tr>
          <td>
            Supplier Description
          </td>
          <td>
            <textarea  id="" cols="30" rows="10" v-model="newSupplier.description" placeholder="write short des..."></textarea>
          </td>
        </tr>

        <tr>
          <td>
            
          </td>
          <td>
            <button class="btnSave" @click="addNewSupplier()">Save</button>
          </td>
        </tr>
      </table>
    </modal>

    <modal modalHeading="Update This Supplier" :cond="showingEditModal" @modalClose="showingEditModal=false">
      <table>
        <tr>
          <td>
            Supplier Name
          </td>
          <td>
            <input type="text" id="newCatName" v-model="clickSupplier.name" placeholder="Supplier Name">
          </td>
        </tr>

        <tr>
          <td>
            Supplier Description
          </td>
          <td>
            <textarea  id="" cols="30" rows="10" v-model="clickSupplier.description" placeholder="write short des..."></textarea>
          </td>
        </tr>

        <tr>
          <td>
            
          </td>
          <td>
            <button class="btnSave" @click="updateSupplier()">Update</button>
          </td>
        </tr>
      </table>
    </modal>

    <modal modalHeading="Are you sure?" :cond="showingDeleteModal" @modalClose="showingDeleteModal=false">
      
      <h2>
        You are going to delete the supplier <b>{{ clickSupplier.name }}</b>
      </h2>
      <table>
        <tr>
          <td>
            <button class="btnSave" @click="deleteSupplier()">Yes</button>
          </td>
          <td>
            <button class="btnClose" @click="showingDeleteModal=false">No</button>
          </td>
        </tr>
      </table>
    </modal>

    <h2 class="fleft">Suppliers</h2>
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

      <tr v-for="(supplier, i) in suppliers" :key="i">
        <td>{{ supplier.id }}</td>
        <td>{{ supplier.name }}</td>
        <td>{{ supplier.description }}</td>
        <td><button class="edit" @click="showingEditModal = true; clickSupplier = supplier">Edit</button></td>
        <td><button class="delete" @click="showingDeleteModal = true; clickSupplier = supplier">Delete</button></td>
      </tr>
    </table>
  </div>
</template>

<script>
export default {
  name: 'Supplier',
  data () {
    return {
      showingAddModal: false,
      showingEditModal: false,
      showingDeleteModal: false,

      newSupplier:{
        name: "",
        description: ""
      },
      clickSupplier: {},
      suppliers: []
    }
  },
  mounted(){
    this.init();
  },
  methods: {
      init(){
        this.$eventBus.$emit("loadingStatus", true);

        this.$axios.get("http://localhost:8000/api/supplier")
          .then(res=> {
            this.$eventBus.$emit("loadingStatus", false);
            this.suppliers = res.data
          })
      },

      addNewSupplier(){

        if(!this.newSupplier.name){
          
          this.$iziToast.error({
              title: 'Error',
              message: "Supplier name can't be empty!" 
            })

            var catNameInput = document.getElementById("newCatName");
            catNameInput.focus();
          return;
        }

        this.$eventBus.$emit("loadingStatus", true);
        this.$axios.post("http://localhost:8000/api/supplier/create", this.newSupplier)
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

      updateSupplier(){
        console.log(this.clickSupplier.id)
        this.$eventBus.$emit("loadingStatus", true);
        this.$axios.put("http://localhost:8000/api/supplier/update/"+this.clickSupplier.id, this.clickSupplier)
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

          this.clickSupplier = {};
          console.log("done")
      },

      deleteSupplier() {
        this.$eventBus.$emit("loadingStatus", true);
        this.$axios.delete("http://localhost:8000/api/supplier/delete/"+this.clickSupplier.id, this.clickSupplier)
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

          this.clickSupplier = {};
          
      }
  }
}
</script>
