const url = 'http://127.0.0.1:5000/generate_tactics';
const proofState = "P Q R : Prop,\nh : P → Q,\nhq : Q → R,\nhqr : P\n⊢ R";
const data = { proof_state: proofState };

fetch(url, {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify(data)
})
  .then(response => {
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    return response.json();
  })
  .then(data => {
    const tacticCandidates = data.tactics;
    tacticCandidates.forEach(tac => {
      console.log(tac);
    });
  })
  .catch(error => {
    console.error('Error:', error);
  });
