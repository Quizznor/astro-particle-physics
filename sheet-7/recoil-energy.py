import matplotlib.pyplot as plt
import numpy as np

m_p = 938.2720813 # MeV

def E_recoil(m_k):

    m_x = 100*m_p
    E_x = m_x*np.sqrt(1-(230/300000)**2)
    return 4*(m_k * m_x)/(m_k + m_x)**2*E_x

M = np.linspace(10*m_p,1000*m_p,100)


plt.xlabel("$m_\mathrm{K}$ ($m_p$)")
plt.ylabel("$E_\mathrm{K}$ (GeV)")
plt.plot(M/m_p,E_recoil(M)*1e-3)

max_ = np.where(E_recoil(M)==max(E_recoil(M)))[0][0]
E_max = max(E_recoil(M))
m_k_max = M[max_]/m_p

plt.scatter(m_k_max,E_max*1e-3,label="$m_\mathrm{K}$ = 100 $m_p$, $E_\mathrm{K}^\mathrm{max}$ = %.2f GeV"%(E_max*1e-3),c="k")
plt.legend()
plt.show()
