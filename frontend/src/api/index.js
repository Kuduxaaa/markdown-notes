import axios from 'axios';

class Posts {
    constructor() {
        axios.defaults.baseURL = 'http://localhost:8001/api/v1/';
    }

    async getAll() {
        try {
            const response = await axios.get('/posts');
            return response.data;

        } catch (error) {
            console.error('Error fetching posts:', error);
            return [];
        }
    }

    async get(id) {
        try {
            const response = await axios.get(`/posts/${id}`);
            return response.data;
        } catch (error) {
            console.error('Error fetching post:', error);
            return null;
        }
    }

    async create(title, content) {
        try {
            const response = await axios.post('/posts', { title, content });
            return response.data;
        } catch (error) {
            console.error('Error creating post:', error);
            return null;
        }
    }

    async update(id, title, content) {
        try {
            const response = await axios({
                method: 'POST',
                url: `/posts/${id}`,
                data: {
                    title: title,
                    content: content
                }
            });

            return response.data;
        } catch (error) {
            console.error('Error updating post:', error);
            return null;
        }
    }



    async deletePost(id) {
        try {
            await axios.delete(`/posts/${id}`);
            return true;
        } catch (error) {
            console.error('Error deleting post:', error);
            return false;
        }
    }
}

export default Posts;
