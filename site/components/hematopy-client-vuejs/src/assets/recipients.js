module.exports = [
  {
    type: 'input',
    inputType: 'file',
    label: 'Foto do Paciênte',
    model: 'recipientImage'
  },
  {
    type: 'text',
    inputType: 'text',
    label: 'Nome do Paciênte',
    model: 'recipientName'
  },
  {
    type: 'select',
    label: 'Tipo Sanguíneo',
    model: 'recipientBloodType',
    values: ['O+', 'A+', 'B+', 'AB+', 'O-', 'A-', 'B-', 'AB-']
  },
  {
    type: 'input',
    inputType: 'text',
    label: 'Endereço',
    model: 'locationAddress'
  },
  {
    question: 'Cidade',
    type: 'text',
    model: 'locationAddressLocality',
    name: 'location-address-locality',
    id: 'location-address-locality'
  },
  {
    question: 'Bairro',
    type: 'text',
    model: 'locationAddressDistrict',
    name: 'location-address-district',
    id: 'location-address-district'
  },
  {
    question: 'Logradouro (Av. Rua, etc)',
    type: 'text',
    model: 'locationAddressStreet',
    name: 'location-address-street',
    id: 'location-address-street'
  },
  {
    question: 'Número',
    type: 'text',
    model: 'locationAddressNumber',
    name: 'location-address-number',
    id: 'location-address-number'
  }
]
