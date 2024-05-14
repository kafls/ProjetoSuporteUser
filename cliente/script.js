async function enviarDados(event) {
    event.preventDefault()//método que bloqueia a ação padrão do formulário, que seria a de recarregar a página limpando os dados do formulário.
  
    const formData = new FormData(document.getElementById('formulario')) //cria um novo objeto FormData e preenche-o com os dados do formulário HTML 
    const response = await fetch('http://127.0.0.1/novo', { 
      method: 'POST',
      body: formData
    })
    
    if (response.status == 201) {
      alert('Chamado cadastrado com sucesso!')
    //   window.location.href = "gestao.html"
      return true
    } else {
      alert('Falha ao cadastrar! Fale com o suporte')
      return false
    }
  }
  
// Example starter JavaScript for disabling form submissions if there are invalid fields
(() => {
    'use strict'

    // Fetch all the forms we want to apply custom Bootstrap validation styles to
    const forms = document.querySelectorAll('.needs-validation')

    // Loop over them and prevent submission
    Array.from(forms).forEach(form => {
      form.addEventListener('submit', event => {
        if (!form.checkValidity()) {
          event.preventDefault()
          event.stopPropagation()
        }

        form.classList.add('was-validated')
      }, false)
    })
  })()

  async function consultarCPF(){
    cpf = parseInt(document.getElementById('cpf').value)
    resultado = document.getElementById('resultado')
    const apiUrl = 'http://127.0.0.1/' + cpf
    const response = await fetch(apiUrl)
    if (!response.ok) {
      alert('Chamado não encontrado!')
    }
    else {
      const data = await response.json()
      console.log(data)
      resultado.innerHTML= `
        <p>Nome: ${data['usuario']}</p>
      `
  
    }
  }
  // --------------------------------------------------------------------------------
