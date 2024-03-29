"""Check that QE calculation can run."""

from ase.build import bulk
from ase.calculators.espresso import Espresso

# Default pseudos can go in ~/espresso/pseudo
# Get these from SSSP http://materialscloud.org/sssp/
PSEUDO = {'Au': 'Au.pbe-n-kjpaw_psl.1.0.0.UPF'}

# Don't forget to
# export ASE_ESPRESSO_COMMAND="mpirun -n 4 $HOME/Compile/q-e/bin/pw.x -in PREFIX.pwi > PREFIX.pwo"
# export ESPRESSO_PSEUDO="/path/to/pseudos"

def main():
    gold = bulk('Au')
    input_data = {'system':{'occupations': 'smearing',
                            'smearing': 'fermi-dirac',
                            'degauss': 0.02}}
    calc = Espresso(pseudopotentials=PSEUDO, input_data=input_data)
    gold.set_calculator(calc)
    gold.get_potential_energy()

    assert calc.get_fermi_level() is not None
    assert calc.get_ibz_k_points() is not None
    assert calc.get_eigenvalues(spin=0, kpt=0) is not None
    assert calc.get_number_of_spins() is not None
    assert calc.get_k_point_weights() is not None

main()
