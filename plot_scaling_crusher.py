import os, sys
import numpy as np 
import matplotlib.pyplot as plt

output_dir = ''
# output_dir = '/Users/bruno/Desktop/'



# Load timing 
file_name = 'scaling_crusher_128_per_gpu.log'
data = np.loadtxt( file_name ).T
n_proc = data[0]
n_steps = data[5] 
time_dt = data[6] / n_steps 
time_hydro = data[7] / n_steps
time_bound = data[8] / n_steps 
time_potential = data[9] / n_steps
time_pot_bound = data[10] / n_steps
time_part_dens = data[11] / n_steps 
time_part_bound = data[12] / n_steps
time_part_dens_bound = data[13] / n_steps
time_adv_part_1 = data[14] / n_steps 
time_adv_part_2 = data[15] / n_steps 
time_chemistry = data[16] / n_steps
time_total = data[17] / n_steps

n_proc_128 = n_proc
time_hydro_128 = time_hydro 
time_gravity_128 = time_potential
time_mpi_128 = time_bound + time_pot_bound + time_part_bound + time_part_dens_bound
time_particles_128 = time_dt + time_part_dens + time_adv_part_1 + time_adv_part_2
time_chemistry_128 = time_chemistry
time_total_128 = time_total

# Load timing 
file_name = 'scaling_crusher_256_per_gpu.log'
data = np.loadtxt( file_name ).T
n_proc = data[0]
n_steps = data[5] 
time_dt = data[6] / n_steps  
time_hydro = data[7] / n_steps
time_bound = data[8] / n_steps 
time_potential = data[9] / n_steps
time_pot_bound = data[10] / n_steps
time_part_dens = data[11] / n_steps 
time_part_bound = data[12] / n_steps
time_part_dens_bound = data[13] / n_steps
time_adv_part_1 = data[14] / n_steps 
time_adv_part_2 = data[15] / n_steps 
time_chemistry = data[16] / n_steps
time_total = data[17] / n_steps

n_proc_256 = n_proc
time_hydro_256 = time_hydro 
time_gravity_256 = time_potential
time_mpi_256 = time_bound + time_pot_bound + time_part_bound + time_part_dens_bound
time_particles_256 = time_dt + time_part_dens + time_adv_part_1 + time_adv_part_2
time_chemistry_256 = time_chemistry
time_total_256 = time_total

# Load timing 
file_name = 'scaling_crusher_368_per_gpu.log'
data = np.loadtxt( file_name ).T
n_proc = data[0]
n_steps = data[5] 
time_dt = data[6] / n_steps 
time_hydro = data[7] / n_steps
time_bound = data[8] / n_steps 
time_potential = data[9] / n_steps
time_pot_bound = data[10] / n_steps
time_part_dens = data[11] / n_steps 
time_part_bound = data[12] / n_steps
time_part_dens_bound = data[13] / n_steps
time_adv_part_1 = data[14] / n_steps 
time_adv_part_2 = data[15] / n_steps 
time_chemistry = data[16] / n_steps
time_total = data[17] / n_steps

n_proc_368 = n_proc
time_hydro_368 = time_hydro 
time_gravity_368 = time_potential
time_mpi_368 = time_bound + time_pot_bound + time_part_bound + time_part_dens_bound
time_particles_368 = time_dt + time_part_dens + time_adv_part_1 + time_adv_part_2
time_chemistry_368 = time_chemistry
time_total_368 = time_total

import matplotlib
matplotlib.rcParams['font.sans-serif'] = "Helvetica"
matplotlib.rcParams['font.family'] = "sans-serif"
matplotlib.rcParams['mathtext.fontset'] = 'cm'
matplotlib.rcParams['mathtext.rm'] = 'serif'

colors = [ 'C0', 'C1', 'C2', 'C3', 'C4', 'k']

nrows, ncols = 1, 1
fig, ax = plt.subplots(nrows=nrows, ncols=ncols, figsize=(6*ncols,6*nrows))

ax.plot( n_proc_128, time_hydro_128,     label='Hydro',c=colors[0]     , ls='-'  )
ax.plot( n_proc_128, time_mpi_128,       label='MPI',c=colors[1]       , ls='-'  )
ax.plot( n_proc_128, time_gravity_128,   label='Poisson',c=colors[2]   , ls='-'  )
ax.plot( n_proc_128, time_particles_128, label='Particles',c=colors[3] , ls='-'  )
ax.plot( n_proc_128, time_chemistry_128, label='Chemistry',c=colors[4] , ls='-'  )
ax.plot( n_proc_128, time_total_128,     label='Total',c=colors[5]     , ls='-'  )

factor = 128**3/256**3
ax.plot( n_proc_256, time_hydro_256 * factor,     c=colors[0], ls='--'  )
ax.plot( n_proc_256, time_mpi_256 * factor,       c=colors[1], ls='--'  )
ax.plot( n_proc_256, time_gravity_256 * factor,   c=colors[2], ls='--'  )
ax.plot( n_proc_256, time_particles_256 * factor, c=colors[3], ls='--'  )
ax.plot( n_proc_256, time_chemistry_256 * factor, c=colors[4], ls='--'  )
ax.plot( n_proc_256, time_total_256 * factor,     c=colors[5], ls='--'  )


factor = 128**3/368**3
ax.plot( n_proc_368, time_hydro_368 * factor,     c=colors[0], ls='dotted'  )
ax.plot( n_proc_368, time_mpi_368 * factor,       c=colors[1], ls='dotted'  )
ax.plot( n_proc_368, time_gravity_368 * factor,   c=colors[2], ls='dotted'  )
ax.plot( n_proc_368, time_particles_368 * factor, c=colors[3], ls='dotted'  )
ax.plot( n_proc_368, time_chemistry_368 * factor, c=colors[4], ls='dotted'  )
ax.plot( n_proc_368, time_total_368 * factor,     c=colors[5], ls='dotted'  )


ax.legend( loc=2, frameon=False, fontsize=11 )

ax.set_xscale('log')
# ax.set_yscale('log')

ax.set_xlabel('Number of GPUs')
ax.set_ylabel(r'Milliseconds per time-step / 128$^3$ / GPU')

figure_name = output_dir + f'cholla_scaling_2022_crusher.png'
fig.savefig( figure_name, bbox_inches='tight', dpi=300, facecolor=fig.get_facecolor() )
print( f'Saved Figure: {figure_name}' )
