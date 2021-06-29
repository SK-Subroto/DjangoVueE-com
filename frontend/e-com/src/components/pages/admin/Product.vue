<template>
  <div>
    <modal modalHeading="Add New Product" :cond="showingAddModal" @modalClose="showingAddModal=false">
      <table>
        <tr>
          <td>
            Product Name
          </td>
          <td>
            <input type="text" id="newCatName" v-model="newProduct.name" placeholder="Product Name">
          </td>
        </tr>

        <tr>
          <td>
            Category
          </td>
          <td>
            <select v-model="newProduct.category">
                <option value="">
                    --Select One--
                </option>
                <option v-for="(c, i) in allCategories" :key="i" :value="c.id">
                    {{ c.name }}
                </option>
            </select>
          </td>
        </tr>

        <tr>
          <td>
            Supplier
          </td>
          <td>
            <select v-model="newProduct.supplier">
                <option value="">
                    --Select One--
                </option>
                <option v-for="(s, i) in allSuppliers" :key="i" :value="s.id">
                    {{ s.name }}
                </option>
            </select>
          </td>
        </tr>

        <tr>
          <td>
            Price
          </td>
          <td>
            <input type="text" v-model="newProduct.price" placeholder="Price">
          </td>
        </tr>

        <tr>
          <td>
            Image
          </td>
          <td>
            <input type="file" id="image" @change="onfileChange">
          </td>
        </tr>

        <tr>
          <td>
          </td>
          <td>
            <progress :value="percent" max="100" v-if="percent != 0 && percent != 100"> </progress>
            <span v-if="percent != 0 && percent != 100"> {{percent}}% </span> <br>
            <img :src="'http://localhost:8000/static' + newProduct.image" alt="No img" class="thumbnile">
          </td>
        </tr>

        <tr>
          <td>
            Product Description
          </td>
          <td>
            <textarea  id="" cols="30" rows="10" v-model="newProduct.description" placeholder="write short des..."></textarea>
          </td>
        </tr>

        <tr>
          <td>
            
          </td>
          <td>
            <button class="btnSave" @click="addNewProduct()">Save</button>
          </td>
        </tr>
      </table>
    </modal>

    <modal modalHeading="Update This Product" :cond="showingEditModal" @modalClose="showingEditModal=false">
      <table>
        <tr>
          <td>
            Product Name
          </td>
          <td>
            <input type="text" v-model="clickProduct.name" placeholder="Product Name">
          </td>
        </tr>

        <tr>
          <td>
            Category
          </td>
          <td>
            <select v-model="clickProduct.category">
                <option value="">
                    --Select One--
                </option>
                <option v-for="(c, i) in allCategories" :key="i" :value="c.id">
                    {{ c.name }}
                </option>
            </select>
          </td>
        </tr>

        <tr>
          <td>
            Supplier
          </td>
          <td>
            <select v-model="clickProduct.supplier">
                <option value="">
                    --Select One--
                </option>
                <option v-for="(s, i) in allSuppliers" :key="i" :value="s.id">
                    {{ s.name }}
                </option>
            </select>
          </td>
        </tr>

        <tr>
          <td>
            Price
          </td>
          <td>
            <input type="text" v-model="clickProduct.price" placeholder="Price">
          </td>
        </tr>

        <!-- <tr>
          <td>
            Image
          </td>
          <td>
            <input type="file" id="image" @change="onfileChange">
          </td>
        </tr> -->

        <tr>
          <td>
          </td>
          <td>
            <progress :value="percent" max="100" v-if="percent != 0 && percent != 100"> </progress>
            <span v-if="percent != 0 && percent != 100"> {{percent}}% </span> <br>
            <img :src="'http://localhost:8000/static' + clickProduct.img" alt="No img" class="thumbnile">
          </td>
        </tr>

        <tr>
          <td>
            Product Description
          </td>
          <td>
            <textarea  id="" cols="30" rows="10" v-model="clickProduct.description" placeholder="write short des..."></textarea>
          </td>
        </tr>

        <tr>
          <td>
            
          </td>
          <td>
            <button class="btnSave" @click="updateProduct()">Update</button>
          </td>
        </tr>
      </table>
    </modal>

    <modal modalHeading="Are you sure?" :cond="showingDeleteModal" @modalClose="showingDeleteModal=false">
      
      <h2>
        You are going to delete the product <b>{{ clickProduct.name }}</b>
      </h2>
      <table>
        <tr>
          <td>
            <button class="btnSave" @click="deleteProduct()">Yes</button>
          </td>
          <td>
            <button class="btnClose" @click="showingDeleteModal=false">No</button>
          </td>
        </tr>
      </table>
    </modal>

    <h2 class="fleft">Products</h2>
    <button class="addBtn fright" @click="showingAddModal=true">Add New</button>
    <div class="clear"></div>
    <hr>

    <table class="nice-table">
      <tr>
        <th>ID</th>
        <th>Image</th>
        <th>Name</th>
        <th>Category</th>
        <th>Supplier</th>
        <th>Description</th>
        <th>Edit</th>
        <th>Delete</th>
      </tr>

      <tr v-for="(product, i) in products" :key="i">
        <td>{{ product.id }}</td>
        <td><img :src="'http://localhost:8000/static'+product.img" alt="no img" class="icon"></td>
        <td>{{ product.name }}</td>
        <td>{{ product.category_name }}</td>
        <td>{{ product.supplier_name }}</td>
        <td>{{ product.description }}</td>
        <td><button class="edit" @click="showingEditModal = true; clickProduct = product">Edit</button></td>
        <td><button class="delete" @click="showingDeleteModal = true; clickProduct = product">Delete</button></td>
      </tr>
    </table>
  </div>
</template>

<script>
export default {
  name: 'Product',
  data () {
    return {
      showingAddModal: false,
      showingEditModal: false,
      showingDeleteModal: false,

      newProduct:{
        name: "",
        description: "",
        supplier: "",
        category: "",
        price: 0,
        image: "/images/default.jpg"
      },
      clickProduct: {},
      products: [],
      allCategories: [],
      allSuppliers: [],
      percent: 0,
    }
  },
  mounted(){
    this.init();
  },
  methods: {
      init(){
        this.$eventBus.$emit("loadingStatus", true);

        this.$axios.get("http://localhost:8000/api/category")
          .then(res=> {
            this.allCategories = res.data
          })

        this.$axios.get("http://localhost:8000/api/supplier")
          .then(res=> {
            this.allSuppliers = res.data
          })

        this.$axios.get("http://localhost:8000/api/product")
          .then(res=> {
            console.log(res.data)
            this.products = res.data
          })
          this.$eventBus.$emit("loadingStatus", false);
      },

      onfileChange(e){
          var _this = this
          var files = e.target.files || e.dataTansfers.files

          var file = files[0]
          var fd = new FormData();
          fd.append("myfile", file, file.name)
          this.$axios.post("http://localhost:8000/api/product/upload_file", fd, {
            onUploadProgress: function(uploadEvent) {
              _this.percent = Math.round((uploadEvent.loaded / uploadEvent.total) * 100);
            }
          })
          .then(res => {
              _this.newProduct.image = res.data.uploadedUrl;
              console.log(res.data.uploadedUrl)
          })
          .catch(err => {
            console.log(err)
          })
          
      },

      addNewProduct(){

        //   console.log(this.newProduct)
        //   return;

        if(!this.newProduct.name){
          
          this.$iziToast.error({
              title: 'Error',
              message: "Product name can't be empty!" 
            })

            var catNameInput = document.getElementById("newCatName");
            catNameInput.focus();
          return;
        }

        this.$eventBus.$emit("loadingStatus", true);
        this.$axios.post("http://localhost:8000/api/product/create", this.newProduct)
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

      async updateProduct(){
        // console.log(this.clickProduct)
        // return
        await this.$eventBus.$emit("loadingStatus", true);
        await this.$axios.put("http://localhost:8000/api/product/update/"+this.clickProduct.id, this.clickProduct)
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
            // this.$eventBus.$emit("loadingStatus", false)
            // this.showingAddModal = false
            this.$iziToast.error({
              title: 'Error',
              message: err.response.data.error 
            })
          })

          // this.showingAddModal = false
          // this.$eventBus.$emit("loadingStatus", false)
          this.clickProduct = {};
      },

      deleteProduct() {
        this.$eventBus.$emit("loadingStatus", true);
        this.$axios.delete("http://localhost:8000/api/product/delete/"+this.clickProduct.id, this.clickProduct)
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

          this.clickProduct = {};
          
      }
  }
}
</script>
