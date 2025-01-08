import React from 'react';
import { QueryClient, QueryClientProvider } from 'react-query';
import TaskList from './components/TaskList';
import TaskForm from './components/TaskForm';
import { Container, Typography, Box } from '@material-ui/core';

const queryClient = new QueryClient();

function App() {
  return (
    <QueryClientProvider client={queryClient}>
      <Container maxWidth="md">
        <Box my={4}>
          <Typography variant="h4" component="h1" gutterBottom>
            Task Manager
          </Typography>
          <TaskForm />
          <Box my={4}>
            <TaskList />
          </Box>
        </Box>
      </Container>
    </QueryClientProvider>
  );
}

export default App;