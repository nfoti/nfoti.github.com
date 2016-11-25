---
layout: post
title: "Change of probability densities and the reparameterization trick"
tags: ['change of variables', 'reparameterization trick']
---

The *reparameterization trick* {% cite kingma:2014:vae --file posts %} has
gained great popularity in the machine learning community as a tool to obtain
unbiased estimates of the gradient of an expectation. There are many great
discussion about the reparameterization trick such as the original paper, or
[this blog post](http://blog.shakirm.com/2015/10/machine-learning-trick-of-the-day-4-reparameterisation-tricks/)
by Shakir Mohamed.
The point of this post is to fill in a small gap that often glossed over when
the reparameterization trick is discussed. 

Using the notation used in {% cite kingma:2014:vae --file posts %}, we are
interested in a density $q(z)$ over $z \in \mathbb{R}^n$ and want
to obtain
an expression for $q(z)dz$ in terms of the distribution of a simpler random
variable $\epsilon \sim p(\epsilon)$ such that $z = g(\epsilon)$ for some
smooth function $g(\cdot)$ with inverse map $\epsilon = g^{-1}(z)$. The
reparameterization trick relies on the fact that when we perform this change of
variables that there is a conservation of probability according to
\begin{equation}
  q(z)|dz| = p(\epsilon)|d\epsilon|,
  \label{eq:conserve}
\end{equation}
where the notation $|dz|$ means the volume of the differential.  

For univariate varibles the conservation of probability is usually justified
heuristically by appealing to the *change of probability* formula
\begin{equation}
  q(z) = p(g^{-1}(z))|\frac{d\epsilon}{dz}|,
  \label{eq:pchangeuni}
\end{equation}
which for scalars $z$ and $\epsilon$ we can multiply both sides by $|dz|$ and
the result follows. However, this heuristic breaks down in the
multivariate setting. Specifically, Eq. \eqref{eq:pchangeuni} becomes
\begin{equation}
  q(z) = p(g^{-1}(z))|\frac{\partial g^{-1}(z)}{\partial z}|
  \label{eq:changeprobmv}
\end{equation}
which does not admit to the same heuristic as in the univariate case.

We can derive a heuristic justification for Eq. \eqref{eq:conserve} using
the intuition underlying the *change of variables theorm* from multivariate
calculus (which turns out to be quite tedious to prove). In particular, first
we will assume that $g$ is a linear function, $L$. If we take a small rectangle
$\Delta \epsilon \subset \mathbb{R}^n$, i.e. a set of the form
$[a_1, b_1] \times \cdots \times [a_n, b_n]$, then
$\Delta z = L(\Delta \epsilon)$ is a paralleliped with volume given by
$|\det L||\Delta \epsilon|$. Similarly, the volume of $\Delta \epsilon$ can be computed from
$\Delta z$ as $|L^{-1}||\Delta z|$.

If $g$ is instead a smooth function with inverse
$g^{-1}$ then $g(\Delta \epsilon)$ is **not** a parallelpiped, however,
Taylor's theorem implies that $g$ is locally well-approximated by a linear function, i.e.
$g(\epsilon') \approx g(\epsilon) + \mathbf{D}g$ where $\mathbf{D}g$ is the matrix of first
derivatives, $(\mathbf{D}g)_{ij} = \frac{\partial g_i}{\partial \epsilon_j}$ and
$\epsilon \in \Delta \epsilon$. Thus, locally $\Delta z = g(\Delta \epsilon)$
is a parallelpiped with volume $|\frac{\partial g(\epsilon)}{\partial
\epsilon}||\Delta \epsilon|$, where $\frac{\partial g(\epsilon)}{\partial \epsilon}$ denotes the
determinant of $\mathbf{D}g$. Similarly, we have that
$|\Delta \epsilon| = |\frac{\partial g^{-1}(z)}{\partial z}||\Delta z|$.
Letting the length of the sides of the rectangles $\Delta z$ and
$\Delta \epsilon$ go to zero yields
$|d\epsilon| = |\frac{\partial \epsilon}{\partial z}||dz|$ and plugging into
Eq. \eqref{eq:chang_prob_mv} results in
\begin{equation}
    q(z)|dz| = p(\epsilon)|\frac{\partial \epsilon}{\partial z}||dz|
    = p(\epsilon)|d\epsilon|.
\end{equation}
This is exactly the conservation of probability that underlies the
reparameterization trick.

#### References
{% bibliography --cited --file posts %}
