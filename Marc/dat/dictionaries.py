
# marc class to element numbers dictionary
class_elems = {'Class1' : [1, 5],
'Class2' : [9, 36],
'Class3' : [2, 6, 37, 38, 50, 196, 201, 228, 229],
'Class4' : [3, 10, 11, 18, 19, 20, 39, 40, 80, 81, 82, 83, 111, 112, 160, 161, 162, 198, 230, 231],
'Class5' : [7, 43, 84, 113, 163],
'Class6' : [64, 65],
'Class7' : [26, 27, 28, 29, 30, 32, 33, 34, 41, 42, 62, 63, 66, 67, 199, 234, 235],
'Class8' : [53, 54, 55, 56, 58, 59, 60, 69, 70, 73,  74],
'Class9' : [21, 35, 44, 236],
'Class10' : [57, 61, 71],
'Class11' : [15, 16, 17],
'Class12' : [45],
'Class13' : [13, 14, 25, 52],
'Class14' : [124, 125, 126, 128, 129, 131, 132, 197, 200, 231, 232],
'Class15' : [127, 130, 133, 233],
'Class16' : [114, 115, 116, 118, 119, 121, 122],
'Class17' : [117, 120, 123],
'Class18' : [134, 135, 164],
'Class19' : [136, 137, 204, 237],
'Class20' : [202, 203, 205, 238],
'Special' : [4, 8, 12, 22, 23, 24, 31, 45, 46, 47, 48, 49, 68, 72, 75, 76, 77, 
78, 79, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102,
103, 104, 105, 106, 107, 108, 109, 110, 138, 139, 140, 142, 143, 144, 145,
146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 165, 166, 167,
168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182,
183, 185, 186, 187, 188, 189, 190, 191, 192, 193, 220, 221, 222, 223, 224,
225, 226, 227]}

# element to its description dictionary
element_desc = {1 : 'Straight Axisymmetric Shell',
2 : 'Axisymmetric Triangular Ring',
3 : 'Plane Stress Quadrilateral',
4 : 'Curved Quadrilateral, Thin-shell Element',
5 : 'Beam Column',
6 : 'Two-dimensional Plane Strain Triangle',
7 : 'Three-dimensional Arbitrarily Distorted Brick',
8 : 'Curved Triangular Shell Element',
9 : 'Three-dimensional Truss',
10 : 'Arbitrary Quadrilateral Axisymmetric Ring',
11 : 'Arbitrary Quadrilateral Plane-strain',
12 : 'Friction And Gap Link Element',
13 : 'Open Section Thin-Walled Beam',
14 : 'Thin-walled Beam in Three Dimensions without Warping',
15 : 'Axisymmetric Shell, Isoparametric Formulation',
16 : 'Curved Beam in Two-dimensions, Isoparametric Formulation',
17 : 'Constant Bending, Three-node Elbow Element',
18 : 'Four-node, Isoparametric Membrane',
19 : 'Generalized Plane Strain Quadrilateral',
20 : 'Axisymmetric Torsional Quadrilateral',
21 : 'Three-dimensional 20-node Brick',
22 : 'Quadratic Thick Shell Element',
23 : 'Three-dimensional 20-node Rebar Element',
24 : 'Curved Quadrilateral Shell Element',
25 : 'Thin-walled Beam in Three-dimensions',
26 : 'Plane Stress, Eight-node Distorted Quadrilateral',
27 : 'Plane Strain, Eight-node Distorted Quadrilateral',
28 : 'Axisymmetric, Eight-node Distorted Quadrilateral',
29 : 'Generalized Plane Strain, Distorted Quadrilateral',
30 : 'Membrane, Eight-node Distorted Quadrilateral',
31 : 'Elastic Curved Pipe (Elbow)/Straight Beam',
32 : 'Plane Strain Eight-node Distorted Quadrilateral, Herrmann Formulation',
33 : 'Axisymmetric, Eight-node Distorted Quadrilateral, Herrmann Formulation',
34 : 'Generalized Plane Strain Distorted Quadrilateral, Herrmann Formulation',
35 : 'Three-dimensional 20-node Brick, Herrmann Formulation',
36 : 'Three-dimensional Link (Heat Transfer Element)',
37 : 'Arbitrary Planar Triangle (Heat Transfer Element)',
38 : 'Arbitrary Axisymmetric Triangle (Heat Transfer Element)',
39 : 'Bilinear Planar Quadrilateral (Heat Transfer Element)',
40 : 'Axisymmetric Bilinear Quadrilateral Element (Heat Transfer Element)',
41 : 'Eight-node Planar Biquadratic Quadrilateral (Heat Transfer Element)',
42 : 'Eight-node Axisymmetric Biquadratic Quadrilateral (Heat Transfer Element)',
43 : 'Three-dimensional Eight-node Brick (Heat Transfer Element)',
44 : 'Three-dimensional 20-node Brick (Heat Transfer Element)',
45 : 'Curved Timoshenko Beam in a Plane',
46 : 'Eight-node Plane Strain Rebar Element',
47 : 'Generalized Plane Strain Rebar Element',
48 : 'Eight-node Axisymmetric Rebar Element',
49 : 'Finite Rotation Linear Thin Shell Element',
50 : 'Three-node Linear Heat Transfer Shell Element',
51 : 'Cable Element',
52 : 'Elastic or Inelastic Beam',
53 : 'Plane Stress, Eight-node Distorted Quadrilateral with Reduced Integration',
54 : 'Plane Strain, Eight-node Distorted Quadrilateral with Reduced Integration',
55 : 'Axisymmetric, Eight-node Distorted Quadrilateral with Reduced Integration',
56 : 'Generalized Plane Strain, Distorted Quadrilateral with Reduced Integration',
57 : 'Three-dimensional 20-node Brick with Reduced Integration',
58 : 'Plane Strain Eight-node Distorted Quadrilateral with Reduced Integration Herrmann Formulation',
59 : 'Axisymmetric, Eight-node Distorted Quadrilateral with Reduced Integration, Herrmann Formulation',
60 : 'Generalized Plane Strain Distorted Quadrilateral with Reduced Integration, Herrmann Formulation',
61 : 'Three-dimensional, 20-node Brick with Reduced Integration, Herrmann Formulation',
62 : 'Axisymmetric, Eight-node Quadrilateral for Arbitrary Loading (Fourier)',
63 : 'Axisymmetric, Eight-node Distorted Quadrilateral for Arbitrary Loading, Herrmann Formulation (Fourier) .',
64 : 'Isoparametric, Three-node Truss',
65 : 'Heat Transfer Element, Three-node Link',
66 : 'Eight-node Axisymmetric Herrmann Quadrilateral with Twist',
67 : 'Eight-node Axisymmetric Quadrilateral with Twist',
68 : 'Elastic, Four-node Shear Panel',
69 : 'Eight-node Planar Biquadratic Quadrilateral with Reduced Integration(Heat Transfer Element) .',
70 : 'Eight-node Axisymmetric Biquadrilateral with Reduced Integration(Heat Transfer Element)',
71 : 'Three-dimensional 20-node Brick with Reduced Integration(Heat Transfer Element)',
72 : 'Bilinear Constrained Shell Element',
73 : 'Axisymmetric, Eight-node Quadrilateral for Arbitrary Loading with Reduced Integration (Fourier)',
74 : 'Axisymmetric, Eight-node Distorted Quadrilateral for Arbitrary Loading, Herrmann Formulation, with Reduced Integration(Fourier)...',
75 : 'Bilinear Thick-shell Element',
76 : 'Thin-walled Beam in Three Dimensions without Warping',
77 : 'Thin-walled Beam in Three Dimensions including Warping',
78 : 'Thin-walled Beam in Three Dimensions without Warping',
79 : 'Thin-walled Beam in Three Dimensions including Warping',
80 : 'Arbitrary Quadrilateral Plane Strain, Herrmann Formulation',
81 : 'Generalized Plane Strain Quadrilateral, Herrmann Formulation',
82 : 'Arbitrary Quadrilateral Axisymmetric Ring, Herrmann Formulation',
83 : 'Axisymmetric Torsional Quadrilateral, Herrmann Formulation',
84 : 'Three-dimensional Arbitrarily Distorted Brick, Herrmann Formulation',
85 : 'Four-node Bilinear Shell (Heat Transfer Element)',
86 : 'Eight-node Curved Shell (Heat Transfer Element)',
87 : 'Three-node Axisymmetric Shell (Heat Transfer Element)',
88 : 'Two-node Axisymmetric Shell (Heat Transfer Element)',
89 : 'Thick Curved Axisymmetric Shell',
90 : 'Thick Curved Axisymmetric Shell – for Arbitrary Loading (Fourier)',
91 : 'Linear Plane Strain Semi-infinite Element',
92 : 'Linear Axisymmetric Semi-infinite Element',
93 : 'Quadratic Plane Strain Semi-infinite Element',
94 : 'Quadratic Axisymmetric Semi-infinite Element',
95 : 'Axisymmetric Quadrilateral with Bending',
96 : 'Axisymmetric, Eight-node Distorted Quadrilateral with Bending',
97 : 'Special Gap and Friction Link for Bending',
98 : 'Elastic or Inelastic Beam with Transverse Shear',
99 : 'Three-dimensional Link (Heat Transfer Element)',
100 : 'Three-dimensional Link (Heat Transfer Element)',
101 : 'Six-node Plane Semi-infinite Heat Transfer Element',
102 : 'Six-node Axisymmetric Semi-infinite Heat Transfer Element',
103 : 'Nine-node Planar Semi-infinite Heat Transfer Element',
104 : 'Nine-node Axisymmetric Semi-infinite Heat Transfer Element',
105 : 'Twelve-node 3-D Semi-infinite Heat Transfer Element',
106 : 'Twenty-seven-node 3-D Semi-infinite Heat Transfer Element',
107 : 'Twelve-node 3-D Semi-infinite Stress Element',
108 : 'Twenty-seven-node 3-D Semi-infinite Stress Element',
109 : 'Eight-node 3-D Magnetostatic Element',
110 : 'Twelve-node 3-D Semi-infinite Magnetostatic Element',
111 : 'Arbitrary Quadrilateral Planar Magnetodynamic',
112 : 'Arbitrary Quadrilateral Axisymmetric Magnetodynamic Ring',
113 : 'Three-dimensional Magnetodynamic Arbitrarily Distorted Brick',
114 : 'Plane Stress Quadrilateral, Reduced Integration',
115 : 'Arbitrary Quadrilateral Plane Strain, Reduced Integration',
116 : 'Arbitrary Quadrilateral Axisymmetric Ring, Reduced Integration',
117 : 'Three-dimensional Arbitrarily Distorted Brick, Reduced Integration',
118 : 'Arbitrary Quadrilateral Plane Strain, Incompressible Formulation with Reduced Integration',
119 : 'Arbitrary Quadrilateral Axisymmetric Ring, Incompressible Formulation with Reduced Integration',
120 : 'Three-dimensional Arbitrarily Distorted Brick, Incompressible Reduced Integration',
121 : 'Planar Bilinear Quadrilateral, Reduced Integration (Heat Transfer Element)',
122 : 'Axisymmetric Bilinear Quadrilateral, Reduced Integration(Heat Transfer Element)',
123 : 'Three-dimensional Eight-node Brick, Reduced Integration(Heat Transfer Element) .',
124 : 'Plane Stress, Six-node Distorted Triangle',
125 : 'Plane Strain, Six-node Distorted Triangle',
126 : 'Axisymmetric, Six-node Distorted Triangle',
127 : 'Three-dimensional Ten-node Tetrahedron',
128 : 'Plane Strain, Six-node Distorted Triangle, Herrmann Formulation',
129 : 'Axisymmetric, Six-node Distorted Triangle, Herrmann Formulation',
130 : 'Three-dimensional Ten-node Tetrahedron, Herrmann Formulation',
131 : 'Planar, Six-node Distorted Triangle (Heat Transfer Element)',
132 : 'Axisymmetric, Six-node Distorted Triangle (Heat Transfer Element)',
133 : 'Three-dimensional Ten-node Tetrahedron (Heat Transfer Element)',
134 : 'Three-dimensional Four-node Tetrahedron',
135 : 'Three-dimensional Four-node Tetrahedron (Heat Transfer Element)',
136 : 'Three-dimensional Arbitrarily Distorted Pentahedral',
137 : 'Three-dimensional Six-node Pentahedral (Heat Transfer Element)',
138 : 'Bilinear Thin-triangular Shell Element',
139 : 'Bilinear Thin-shell Element',
140 : 'Bilinear Thick-shell Element with One-point Quadrature',
141 : 'Heat Transfer Shell',
142 : 'Eight-node Axisymmetric Rebar Element with Twist',
143 : 'Four-node Plane Strain Rebar Element',
144 : 'Four-node Axisymmetric Rebar Element',
145 : 'Four-node Axisymmetric Rebar Element with Twist',
146 : 'Three-dimensional 8-node Rebar Element',
147 : 'Four-node Rebar Membrane',
148 : 'Eight-node Rebar Membrane',
149 : 'Three-dimensional, Eight-node Composite Brick Element',
150 : 'Three-dimensional, Twenty-node Composite Brick Element',
151 : 'Quadrilateral, Plane Strain, Four-node Composite Element',
152 : 'Quadrilateral, Axisymmetric, Four-node Composite Element',
153 : 'Quadrilateral, Plane Strain, Eight-node Composite Element',
154 : 'Quadrilateral, Axisymmetric, Eight-node Composite Element',
155 : 'Plane Strain, Low-order, Triangular Element, Herrmann Formulations',
156 : 'Axisymmetric, Low-order, Triangular Element, Herrmann Formulations',
157 : 'Three-dimensional, Low-order, Tetrahedron, Herrmann Formulations',
158 : 'Three-node Membrane Element',
159 : 'Four-node, Thick Shell Element',
160 : 'Arbitrary Plane Stress Piezoelectric Quadrilateral',
161 : 'Arbitrary Plane Strain Piezoelectric Quadrilateral',
162 : 'Arbitrary Quadrilateral Piezoelectric Axisymmetric Ring',
163 : 'Three-dimensional Piezoelectric Arbitrary Distorted Brick',
164 : 'Three-dimensional Four-node Piezo-Electric Tetrahedron',
165 : 'Two-node Plane Strain Rebar Membrane Element',
166 : 'Two-node Axisymmetric Rebar Membrane Element',
167 : 'Two-node Axisymmetric Rebar Membrane Element with Twist',
168 : 'Three-node Plane Strain Rebar Membrane Element',
169 : 'Three-node Axisymmetric Rebar Membrane Element',
170 : 'Three-node Axisymmetric Rebar Membrane Element with Twist',
171 : 'Two-node 2-D Cavity Surface Element',
172 : 'Two-node Axisymmetric Cavity Surface Element',
173 : 'Three-node 3-D Cavity Surface Element',
174 : 'Four-node 3-D Cavity Surface Element',
175 : 'Three-dimensional, Eight-node Composite Brick Element(Heat Transfer Element)',
176 : 'Three-dimensional, Twenty-node Composite Brick Element(Heat Transfer Element)',
177 : 'Quadrilateral Planar Four-node Composite Element(Heat Transfer Element)',
178 : 'Quadrilateral, Axisymmetric, Four-node Composite Element(Heat Transfer Element)',
179 : 'Quadrilateral, Planar Eight-node Composite Element(Heat Transfer Element)',
180 : 'Quadrilateral, Axisymmetric, Eight-node Composite Element(Heat Transfer Element)',
181 : 'Three-dimensional Four-node Magnetostatic Tetrahedron',
182 : 'Three-dimensional Ten-node Magnetostatic Tetrahedron',
183 : 'Three-dimensional Magnetostatic Current Carrying Wire',
184 : 'Three-dimensional Ten-node Tetrahedron',
185 : 'Three-dimensional Eight-node Solid Shell, Selective Reduced Integration',
186 : 'Four-node Planar Interface Element',
187 : 'Eight-node Planar Interface Element',
188 : 'Eight-node Three-dimensional Interface Element',
189 : 'Twenty-node Three-dimensional Interface Element',
190 : 'Four-node Axisymmetric Interface Element',
191 : 'Eight-node Axisymmetric Interface Element',
192 : 'Six-node Three-dimensional Interface Element',
193 : 'Fifteen-node Three-dimensional Interface Element',
194 : '2-D Generalized Spring - CBUSH/CFAST Element',
195 : '3-D Generalized Spring - CBUSH/CFAST Element',
196 : 'Three-node, Bilinear Heat Transfer Membrane',
197 : 'Six-node, Biquadratic Heat Transfer Membrane',
198 : 'Four-node, Isoparametric Heat Transfer Element',
199 : 'Eight-node, Biquadratic Heat Transfer Membrane',
200 : 'Six-node, Biquadratic Isoparametric Membrane',
201 : 'Two-dimensional Plane Stress Triangle',
202 : 'Three-dimensional Fifteen-node Pentahedral',
203 : 'Three-dimensional Fifteen-node Pentahedral (Heat Transfer Element)',
204 : 'Three-dimensional Magnetostatic Pentahedral',
205 : 'Three-dimensional Fifteen-node Magnetostatic Pentahedral',
206 : 'Twenty-node 3-D Magnetostatic Element',
207 : 'Not Available',
208 : 'Not Available',
209 : 'Not Available',
210 : 'Not Available',
211 : 'Not Available',
212 : 'Not Available',
213 : 'Not Available',
214 : 'Not Available',
215 : 'Not Available',
216 : 'Not Available',
217 : 'Not Available',
218 : 'Not Available',
219 : 'Not Available',
220 : 'Four-node Planar Heat Transfer Interface Element',
221 : 'Eight-node Planar Heat Transfer Interface Element',
222 : 'Eight-node Three-dimensional Heat Transfer Interface Element',
223 : 'Twenty-node Three-dimensional Heat Transfer Interface Element',
224 : 'Four-node Axisymmetric Heat Transfer Interface Element',
225 : 'Eight-node Axisymmetric Heat Transfer Interface Element',
226 : 'Six-node Three-dimensional Heat Transfer Interface Element',
227 : 'Fifteen-node Three-dimensional Heat Transfer Interface Element',
228 : 'Arbitrary Triangle Planar Magnetodynamic',
229 : 'Arbitrary Triangle Axisymmetric Magnetodynamic Ring',
230 : 'Three-dimensional Magnetodynamic Arbitrarily Distorted Tetrahedral',
231 : 'Arbitrary Triangle Planar Magnetodynamic',
232 : 'Arbitrary Triangle Axisymmetric Magnetodynamic Ring',
233 : 'Three-dimensional Magnetodynamic Arbitrarily Distorted Tetrahedral',
234 : 'Arbitrary Quadrilateral Planar Magnetodynamic',
235 : 'Arbitrary Quadrilateral Axisymmetric Magnetodynamic Ring',
236 : 'Three-dimensional Magnetodynamic Arbitrarily Distorted Brick',
237 : 'Three-dimensional Magnetodynamic Arbitrarily Distorted Pentahedral',
238 : 'Three-dimensional Magnetodynamic Arbitrarily Distorted Pentahedral'}

# element number to its properties, dictionary
# elem type : number of nodes
#             number of direct stress
#             number of shear stress
#             number of integration points,
#             number of degrees of freedom
#             number of coordinates
#             updated lagrange available
elem_property = {1 : [2, 2, 1, 1, 3, 2, "Yes"],
2 : [3, 3, 1, 1, 2, 2, "Yes"],
3 : [4, 2, 1, 4, 2, 2, "Yes"],
4 : [4, 2, 1, 9, 12, 14, "Yes"],
5 : [2, 1, 1, 3, 3, 2, "No"],
6 : [3, 3, 1, 1, 2, 2, "Yes"],
7 : [8, 3, 3, 8, 3, 3, "Yes"],
8 : [3, 2, 1, 7, 9, 11, "Yes"],
9 : [2, 1, 0, 1, "2/3", "2/3", "Yes"],
10 : [4, 3, 1, 4, 2, 2, "Yes"],
11 : [4, 3, 1, 4, 2, 2, "Yes"],
12 : [4, 1, 2, 1, "2/3", "2/3", "No"],
13 : [2, 1, 0, 3, 8, 13, "No"],
14 : [2, 1, 1, 3, 6, 6, "Yes"],
15 : [2, 2, 0, 3, 4, 5, "Yes"],
16 : [2, 1, 0, 3, 4, 5, "Yes"],
17 : [3, 2, 0, 3, 6, 5, "No"],
18 : [4, 2, 1, 4, 3, 3, "No"],
19 : [6, 3, 1, 4, 2, 2, "Yes"],
20 : [4, 3, 3, 4, 3, 2, "Yes"],
21 : [20, 3, 3, 27, 3, 3, "Yes"],
22 : [8, 2, 3, 4, 6, 3, "Yes"],
23 : [20, 1, 0, 20, 3, 3, "No"],
24 : [8, 2, 1, 28, 9, 11, "Yes"],
25 : [2, 1, 1, 3, 7, 6, "Yes"],
26 : [8, 2, 1, 9, 2, 2, "Yes"],
27 : [8, 3, 1, 9, 2, 2, "Yes"],
28 : [8, 3, 1, 9, 2, 2, "Yes"],
29 : [10, 3, 1, 9, 2, 2, "Yes"],
30 : [8, 2, 1, 9, 3, 3, "No"],
31 : [2, 2, 1, 2, 6, 3, "No"],
32 : [8, 3, 1, 9, 3, 2, "Yes"],
33 : [8, 3, 1, 9, 3, 2, "Yes"],
34 : [10, 3, 1, 9, 3, 2, "Yes"],
35 : [20, 3, 3, 27, 4, 3, "Yes"],
36 : [2, 1, 0, 1, 1, 3, "No"],
37 : [3, 2, 0, 1, 1, 2, "No"],
38 : [3, 2, 0, 1, 1, 2, "No"],
39 : [4, 2, 0, 4, 1, 2, "No"],
40 : [4, 2, 0, 4, 1, 2, "No"],
41 : [8, 2, 0, 9, 1, 2, "No"],
42 : [8, 2, 0, 9, 1, 2, "No"],
43 : [8, 3, 0, 8, 1, 3, "No"],
44 : [20, 3, 0, 27, 1, 3, "No"],
45 : [3, 1, 1, 2, 3, 2, "Yes"],
46 : [8, 1, 0, 10, 2, 2, "No"],
47 : [10, 1, 0, 10, 2, 2, "No"],
48 : [8, 1, 0, 10, 2, 2, "No"],
49 : [6, 2, 1, 1, 3, 3, "Yes"],
50 : [3, 3, 0, 1, 2, 3, "No"],
51 : [2, 1, 0, 1, 3, 3, "No"],
52 : [2, 1, 0, 3, 6, 6, "Yes"],
53 : [8, 2, 1, 4, 2, 2, "Yes"],
54 : [8, 3, 1, 4, 2, 2, "Yes"],
55 : [8, 3, 1, 4, 2, 2, "Yes"],
56 : [10, 3, 1, 4, 2, 2, "Yes"],
57 : [20, 3, 3, 8, 3, 3, "Yes"],
58 : [8, 3, 1, 4, 3, 2, "Yes"],
59 : [8, 3, 1, 4, 3, 2, "Yes"],
60 : [10, 3, 1, 4, 3, 2, "Yes"],
61 : [20, 3, 3, 8, 4, 3, "Yes"],
62 : [8, 3, 3, 9, 3, 2, "No"],
63 : [8, 3, 3, 9, 4, 2, "No"],
64 : [3, 1, 0, 3, 3, 3, "Yes"],
65 : [3, 1, 0, 3, 1, 3, "No"],
66 : [8, 3, 3, 9, 4, 2, "No"],
67 : [8, 3, 3, 9, 3, 2, "No"],
68 : [4, 0, 1, 1, 3, 3, "No"],
69 : [8, 2, 0, 4, 1, 2, "No"],
70 : [8, 2, 0, 4, 1, 2, "No"],
71 : [20, 3, 0, 8, 1, 3, "No"],
72 : [8, 2, 1, 4, 3, 3, "Yes"],
73 : [8, 3, 3, 4, 3, 2, "No"],
74 : [8, 3, 3, 4, 4, 2, "No"],
75 : [4, 2, 3, 4, 6, 3, "Yes"],
76 : [3, 1, 1, 2, 6, 6, "Yes"],
77 : [3, 1, 0, 2, 7, 6, "Yes"],
78 : [2, 1, 1, 2, 6, 6, "Yes"],
79 : [2, 1, 0, 2, 7, 6, "Yes"],
80 : [5, 3, 1, 4, 2, 2, "Yes"],
81 : [7, 3, 1, 4, 2, 2, "Yes"],
82 : [5, 3, 1, 4, 2, 2, "Yes"],
83 : [5, 3, 3, 4, 3, 2, "Yes"],
84 : [9, 3, 3, 8, 3, 3, "Yes"],
85 : [4, 3, 0, 4, "2/3", 3, "No"],
86 : [8, 3, 0, 9, "2/3", 3, "No"],
87 : [3, 2, 0, 3, "2/3", 2, "No"],
88 : [2, 2, 0, 3, "2/3", 2, "No"],
89 : [3, 2, 1, 2, 3, 2, "Yes"],
90 : [3, 2, 3, 2, 5, 2, "No"],
91 : [6, 3, 1, 6, 2, 2, "No"],
92 : [6, 3, 1, 6, 2, 2, "No"],
93 : [9, 3, 1, 9, 2, 2, "No"],
94 : [9, 3, 1, 9, 2, 2, "No"],
95 : [4, 3, 3, 4, 5, 2, "No"],
96 : [8, 3, 3, 9, 5, 2, "No"],
97 : [4, 2, 2, 1, 4, 2, "No"],
98 : [2, 1, 2, 1, 6, 6, "Yes"],
101 : [6, 2, 0, 6, 1, 2, "No"],
102 : [6, 2, 0, 6, 1, 2, "No"],
103 : [9, 2, 0, 9, 1, 2, "No"],
104 : [9, 2, 0, 9, 1, 2, "No"],
105 : [12, 3, 0, 12, 1, 3, "No"],
106 : [27, 3, 0, 27, 1, 3, "No"],
107 : [12, 3, 3, 12, 3, 3, "No"],
108 : [27, 3, 3, 27, 3, 3, "No"],
109 : [8, 3, 0, 8, 3, 3, "No"],
110 : [12, 3, 0, 12, 3, 3, "No"],
111 : [4, 2, 0, 4, 4, 2, "No"],
112 : [4, 2, 0, 4, 4, 2, "No"],
113 : [8, 3, 0, 8, 4, 3, "No"],
114 : [4, 2, 1, 1, 2, 2, "Yes"],
115 : [4, 3, 1, 1, 2, 2, "Yes"],
116 : [4, 3, 1, 1, 2, 2, "Yes"],
117 : [8, 3, 3, 1, 3, 3, "Yes"],
118 : [5, 3, 1, 1, 2, 2, "No"],
119 : [5, 3, 1, 1, 2, 2, "No"],
120 : [9, 3, 3, 1, 3, 3, "No"],
121 : [4, 2, 0, 1, 1, 2, "No"],
122 : [4, 2, 0, 1, 1, 2, "No"],
123 : [8, 3, 0, 1, 1, 3, "No"],
124 : [6, 2, 1, 3, 2, 2, "Yes"],
125 : [6, 3, 1, 3, 2, 2, "Yes"],
126 : [6, 3, 1, 3, 2, 2, "Yes"],
127 : [10, 3, 3, 4, 3, 3, "Yes"],
128 : [6, 3, 1, 3, 3, 2, "No"],
129 : [6, 3, 1, 3, 3, 2, "No"],
130 : [10, 3, 3, 4, 4, 3, "No"],
131 : [6, 2, 0, 3, 1, 2, "No"],
132 : [6, 2, 0, 3, 1, 2, "No"],
133 : [10, 3, 0, 4, 1, 3, "No"],
134 : [4, 3, 3, 1, 3, 3, "Yes"],
135 : [4, 3, 0, 1, 1, 3, "No"],
136 : [6, 3, 3, 6, 3, 3, "Yes"],
137 : [6, 3, 0, 6, 1, 3, "No"],
138 : [3, 2, 1, 1, 6, 3, "Yes"],
139 : [4, 2, 1, 4, 6, 3, "Yes"],
140 : [4, 2, 3, 1, 6, 3, "Yes"],
141 : ["Not Available"],
142 : [8, 1, 0, 10, 3, 2, "No"],
143 : [4, 1, 0, 10, 2, 2, "No"],
144 : [4, 1, 0, 10, 2, 2, "No"],
145 : [4, 1, 0, 10, 3, 2, "No"],
146 : [8, 1, 0, 20, 3, 3, "No"],
147 : [4, 1, 0, 20, 3, 3, "No"],
148 : [8, 1, 0, 20, 3, 3, "No"],
149 : [8, 3, 3, "up to 2040", 3, 3, "Yes"],
150 : [20, 3, 3, "up to 2040", 3, 3, "Yes"],
151 : [4, 3, 1, "up to 2040", 2, 2, "Yes"],
152 : [4, 3, 1, "up to 2040", 2, 2, "Yes"],
153 : [8, 3, 1, "up to 2040", 2, 2, "Yes"],
154 : [8, 3, 1, 10, 2, 2, "Yes"],
155 : ["3 + 1", 3, 1, 3, 3, 2, "Yes"],
156 : ["3 + 1", 3, 1, 3, 3, 2, "Yes"],
157 : ["4 + 1", 3, 3, 4, 4, 3, "Yes"],
158 : [3, 2, 1, 1, 3, 3, "No"],
159 : ["Not Available"],
160 : [4, 2, 1, 4, 3, 2, "No"],
161 : [4, 3, 1, 4, 3, 2, "No"],
162 : [4, 3, 1, 4, 3, 2, "No"],
163 : [8, 3, 3, 8, 4, 3, "No"],
164 : [4, 3, 3, 1, 4, 3, "No"],
165 : [2, 1, 0, 10, 2, 2, "No"],
166 : [2, 1, 0, 10, 2, 2, "No"],
167 : [2, 1, 0, 10, 3, 2, "No"],
168 : [3, 1, 0, 10, 2, 2, "No"],
169 : [3, 1, 0, 10, 2, 2, "No"],
170 : [3, 1, 0, 10, 3, 2, "No"],
171 : [2, 0, 0, 0, 2, 2, "No"],
172 : [2, 0, 0, 0, 2, 2, "No"],
173 : [3, 0, 0, 0, 3, 3, "No"],
174 : [4, 0, 0, 0, 3, 3, "No"],
175 : [8, 3, 0, "up to 2040", 1, 3, "No"],
176 : [20, 3, 0, "up to 2040", 1, 3, "No"],
177 : [4, 2, 0, "up to 2040", 1, 2, "No"],
178 : [4, 2, 0, "up to 2040", 1, 2, "No"],
179 : [8, 2, 0, "up to 2040", 1, 2, "No"],
180 : [8, 2, 0, "up to 2040", 1, 2, "No"],
181 : [4, 3, 0, 1, 3, 3, "No"],
182 : [10, 3, 0, 4, 3, 3, "No"],
183 : [2, 0, 0, 0, 3, 3, "No"],
184 : [10, 3, 3, 4, 3, 3, "Yes"],
185 : [8, 3, 3, "Number of Layers", 3, 3, "Yes"],
186 : [4, 1, 1, 2, 2, 2, "Yes"],
187 : [8, 1, 1, 3, 2, 2, "Yes"],
188 : [8, 1, 2, 4, 3, 3, "Yes"],
189 : [20, 1, 2, "8/9", 3, 3, "Yes"],
190 : [4, 1, 1, 2, 2, 2, "Yes"],
191 : [8, 1, 1, 3, 2, 2, "Yes"],
192 : [6, 1, 2, 3, 3, 3, "Yes"],
193 : [6, 1, 2, "6/7", 3, 3, "Yes"],
194 : [2, 2, 1, 1, 2, 2, "Yes*"],
195 : [2, 3, 3, 1, 3, 3, "Yes*"],
196 : [3, 2, 0, 1, 1, 3, "No"],
197 : [6, 2, 0, 7, 1, 3, "No"],
198 : [4, 2, 0, 4, 1, 3, "No"],
199 : [8, 2, 0, 9, 1, 3, "No"],
200 : [6, 2, 1, 7, 3, 3, "No"],
201 : [3, 2, 1, 1, 2, 2, "Yes"],
202 : [15, 3, 3, 21, 3, 3, "Yes"],
203 : [15, 3, 0, 21, 1, 3, "No"],
204 : [6, 3, 0, 6, 3, 3, "No"],
205 : [15, 3, 0, 21, 3, 3, "No"],
206 : [20, 3, 0, 27, 3, 3, "No"],
220 : [4, 1, 0, 2, 1, 2, "Yes"],
221 : [8, 1, 0, 3, 1, 2, "Yes"],
222 : [8, 1, 0, 4, 1, 3, "Yes"],
223 : [20, 1, 0, "8/9", 1, 3, "Yes"],
224 : [4, 1, 0, 2, 1, 2, "Yes"],
225 : [8, 1, 0, 3, 1, 2, "Yes"],
226 : [6, 1, 0, 3, 1, 3, "Yes"],
227 : [6, 1, 0, "6/7", 1, 3, "Yes"],
228 : [3, 2, 0, 1, 4, 2, "No"],
229 : [3, 2, 0, 1, 4, 2, "No"],
230 : [4, 3, 0, 1, 4, 3, "No"],
231 : [6, 2, 0, 3, 4, 2, "No"],
232 : [6, 2, 0, 3, 3, 2, "No"],
233 : [10, 3, 0, 4, 4, 3, "No"],
234 : [8, 2, 0, 9, 4, 2, "No"],
235 : [8, 2, 0, 9, 4, 2, "No"],
236 : [20, 3, 0, 27, 4, 3, "No"],
237 : [6, 3, 0, 6, 4, 3, "No"],
238 : [15, 3, 0, 18, 4, 3, "No"]}

# analysis type to suitable elemenets, dictionary
solntype_suitable_elems = {'ELASTIC' : [21, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 67, 68, 73, 74, 98, 124, 125, 126, 127, 184],
'DESIGN SENSITIVITY'  : [],
'DESIGN OPTIMIZATION' : [],
'ADAPTIVE'            : [2, 3, 6, 7, 10, 11, 18, 19, 20, 37, 38, 39, 40, 43, 75, 80, 81, 82, 83, 84, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 139, 140, 196, 198, 201],
'LINEAR'              : [],
'FOURIER'             : [62, 63, 73, 74, 90],
'DYNAMIC'             : [2, 3, 5, 6, 7, 9, 10, 11, 17, 18, 19, 20, 31, 52, 64, 75, 98, 114, 115, 116, 117, 118, 119, 120],
'HARMONIC'            : [111, 112, 113, 160, 161, 162, 163, 164, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238],
'SS-ROLLING'          : [],
'RESPONSE'            : [],
'R-P FLOW'            : [],
'SPFLOW'              : [],
'LARGE DISP'          : [18, 30, 49, 158, 200],
'LARGE STRAIN'        : [32, 33, 34, 35, 58, 59, 60, 61, 63, 66, 74, 80, 81, 82, 83, 84, 118, 119, 120, 128, 129, 130, 155, 156, 157],
'UPDATE'              : [],
'FINITE'              : [],
'CONSTANT DILATATION' : [7, 10, 11, 19, 20, 136, 149, 151, 152],
'ASSUMED STRAIN'      : [3, 7, 11, 160, 161, 163, 185],
'ELASTICITY'          : [32, 33, 34, 35, 58, 59, 60, 61, 63, 66, 74, 80, 81, 82, 83, 84, 118, 119, 120, 128, 129, 130, 155, 156, 157],
'PLASTICITY'          : [32, 33, 34, 35, 58, 59, 60, 61, 63, 66, 74, 80, 81, 82, 83, 84, 118, 119, 120, 128, 129, 130, 155, 156, 157],
'FOLLOW FOR'          : [3, 7, 10, 11, 18, 72, 75, 80, 82, 84, 114, 115, 116, 117, 118, 119, 120, 139, 140, 149, 151, 152, 160, 161, 162, 163, 185],
'BUCKLE'              : [],
'CREEP'               : [7, 10, 11, 13, 14, 17, 19, 20, 25, 52, 72, 75, 76, 77, 78, 79, 89, 90, 95, 96, 98, 136, 138, 139, 140],
'VISCO ELAS'          : [],
'STRUCTURAL'          : [],
'COUPLE'              : [],
'DECOUPLING'          : [],
'FLUID'               : [],
'PORE'                : [41, 42, 44, 27, 28, 21, 32, 33, 35],
'T-T-T'               : [],
'HEAT'                : [36, 37, 38, 39, 40, 41, 42, 43, 44, 50, 65, 69, 70, 71, 85, 86, 87, 88, 101, 102, 103, 104, 105, 106, 121, 122, 123, 131, 132, 133, 135, 136, 175, 176, 177, 178, 179, 180, 196, 197, 198, 199, 203, 220, 221, 222, 223, 224, 225, 226, 227],	
'JOULE'               : [36, 37, 38, 39, 40, 41, 42, 43, 44, 65, 69, 70, 71, 121, 122, 123, 131, 132, 133, 135, 136, 175, 176, 177, 178, 179, 180, 196, 197, 198, 199, 203],
'DIFFUSION'           : [],
'ABLATION'            : [],
'PYROLYSIS'           : [],
'CURING'              : [221, 222, 223, 224, 225, 226, 227, 220],
'BEARING'             : [],
'ELECTRO'             : [37, 38, 39, 40, 41, 42, 43, 44, 50, 69, 70, 71, 85, 86, 87, 88, 101, 102, 103, 104, 105, 106, 121, 122, 123, 131, 132, 133, 135, 136, 175, 176, 177, 178, 179, 180, 196, 197, 198, 199, 203],
'MAGNETO'             : [37, 38, 39, 40, 41, 42, 69, 70, 101, 102, 103, 104, 109, 110, 121, 122, 131, 132, 177, 178, 179, 180, 181, 182, 183],
'EL-MA'               : [],
'PIEZO'               : [160, 161, 162, 163, 164],
'ACOUSTIC'            : [],
'RADIATION'           : [36, 40, 42, 70, 99, 100, 122],
'CAVITY'              : [],
'RBE'                 : [],
'MACHINING'           : []}

# analysis type to not suitable elemenets, dictionary
solntype_unsuitable_elems = {'ELASTIC' : [],
'DESIGN SENSITIVITY'  : [],
'DESIGN OPTIMIZATION' : [],
'ADAPTIVE'            : [],
'LINEAR'              : [],
'FOURIER'             : [],
'DYNAMIC'             : [],
'HARMONIC'            : [],
'SS-ROLLING'          : [],
'RESPONSE'            : [],
'R-P FLOW'            : [],
'SPFLOW'              : [],
'LARGE DISP'          : [],
'LARGE STRAIN'        : [],
'UPDATE'              : [],
'FINITE'              : [],
'CONSTANT DILATATION' : [],
'ASSUMED STRAIN'      : [],
'ELASTICITY'          : [],
'PLASTICITY'          : [],
'FOLLOW FOR'          : [],
'BUCKLE'              : [],
'CREEP'               : [],
'VISCO ELAS'          : [],
'STRUCTURAL'          : [],
'COUPLE'              : [],
'DECOUPLING'          : [],
'FLUID'               : [],
'PORE'                : [],
'T-T-T'               : [],
'HEAT'                : [],
'JOULE'               : [],
'DIFFUSION'           : [],
'ABLATION'            : [],
'PYROLYSIS'           : [],
'CURING'              : [],
'BEARING'             : [],
'ELECTRO'             : [],
'MAGNETO'             : [],
'EL-MA'               : [],
'PIEZO'               : [],
'ACOUSTIC'            : [],
'RADIATION'           : [],
'CAVITY'              : [],
'RBE'                 : [],
'MACHINING'           : []}

# dictionary to find analysis name, with relevant card
sol_name_cards = {'Elastic analysis with multi-loads' : 'ELASTIC',
'Sensitivity analysis'                                    : 'DESIGN SENSITIVITY',
'Dynamic analysis'                                        : 'DYNAMIC',
'Frequency response analysis'                             : 'HARMONIC',
'Steady state transport analysis'                         : 'SS-ROLLING',
'Spectrum response analysis'                              : 'RESPONSE',
'Rigid, perfectly-plastic flow analysis'                  : 'R-P FLOW',
'Superplastic forming analysis'                           : 'SPFLOW',
'Large displacement or buckling analysis'                 : 'LARGE DISP',
'Large strain analysis with updated lagrange formulation' : 'LARGE STRAIN',
#'Large strain analysis with updated lagrange formulation' : 'LARGE STRA', # in this repition, 'LARGE STRA' is taken as value for this key    
'Eigenvalue analysis'                                     : 'BUCKLE',
'Creep analysis'                                          : 'CREEP',
'Visco elastic analysis (Kelvin model)'                   : 'VISCO ELAS',
'Mechanical analysis'                                     : 'STRUCTURAL',
'Coupled Thermal-Stress Analysis'                         : 'COUPLE',
'Contact Decoupling Analysis'                             : 'DECOUPLING',
'Fluid analysis'                                          : 'FLUID',
'Soil analysis'                                           : 'PORE',
'Heat transfer (conduction) analysis'                     : 'HEAT',
'Joule heating (coupled thermo-electrical) analysis'      : 'JOULE',
'Diffusion analysis'                                      : 'DIFFUSION',
'Bearing analysis'                                        : 'BEARING',
'Electrostatic analysis'                                  : 'ELECTRO',
'Magnetostatic analysis'                                  : 'MAGNETO',
'Magnetodynamic analysis'                                 : 'EL-MA',
'Piezoelectric analysis'                                  : 'PIEZO',
'Acoustic analysis'                                       : 'ACOUSTIC',
'Radiation analysis'                                      : 'RADIATION',
'NC Machining (Metal Cutting) Process Analysis'           : 'MACHINING',
}


# dictionary to find multiphysics name, with card combinations
multiphysics_name_cards = {'Coupled thermo-mechanical analysis'             : ['STRUCTURAL', 'HEAT'],
'Cure-thermo-mechanically coupled analysis'      : ['STRUCTURAL', 'HEAT', 'CURING'],
'Coupled thermo-electrical resistance analysis'  : ['STRUCTURAL', 'JOULE'],
'Joule heating - resistive heating analysis'     : ['HEAT', 'JOULE'],
'Coupled thermo-mechanical-electrical problem'   : ['STRUCTURAL', 'HEAT', 'JOULE'],    # structural is used
'Coupled thermo-mechanical-electrical problem'   : ['COUPLE', 'HEAT', 'JOULE'],        # couple is used
'Fluid-thermal analysis'                         : ['FLUID', 'HEAT'],
'Fluid-solid analysis'                           : ['FLUID', 'STRUCTURAL'],
'Fluid-thermal-solid analysis'                   : ['FLUID', 'HEAT', 'STRUCTURAL'],
'Thermo-poro-ablative model analysis'            : ['ABLATION', 'PYROLYSIS'],
'Coulomb force calculation'                      : ['STRUCTURAL', 'ELECTRO'],
'Resistance heating analysis'                    : ['ELECTRO', 'HEAT'],
'Lorenzi force calculation'                      : ['STRUCTURAL', 'MAGNETO'],
'Resistance and Eddy current heating'            : ['MAGNETO', 'HEAT'],
'Induction heating simulation'                   : ['EL-MA', 'HEAT'],
'Coupled structural-acoustic analysis'           : ['STRUCTURAL', 'ACOUSTIC'],
'Structural analysis with piezoelectric effects' : ['STRUCTURAL', 'PIEZO']
}

# analysis options and related parameters (soln options are not added in values)
solopts_related_cards = {
'ELASTIC'             : ['POINT LOAD', 'DISTLOADS', 'CHANGE STATE', 'THERMAL LOADS', 'ADAPTIVE'],
'DESIGN SENSITIVITY'  : ['DESIGN VARIABLES', 'DESIGN DISPLACEMENT CONSTRAINTS', 'DESIGN STRESS CONSTRAINTS', 'DESIGN STRAIN CONSTRAINTS', 'DESIGN FREQUENCY CONSTRAINTS', 'ELASTIC'],
'DESIGN OPTIMIZATION' : ['DESIGN OBJECTIVE', 'DESIGN VARIABLES', 'DESIGN DISPLACEMENT CONSTRAINTS', 'DESIGN STRESS CONSTRAINTS', 'DESIGN STRAIN CONSTRAINTS', 'DESIGN FREQUENCY CONSTRAINTS', 'ELASTIC'],
'ADAPTIVE'            : ['ELASTIC', 'ADAPT GLOBAL', 'REZONING'], # is ADAPT GLOBAL there?
'LINEAR'              : [],
'FOURIER'             : ['DYNAMIC', 'BUCKLE', 'CASE COMBIN'],
'DYNAMIC'             : ['MODAL SHAPE', 'MODAL INCREMENT', 'DYNAMIC CHANGE', 'AUTO STEP', 'RECOVER', 'CONTROL', 'PARAMETERS'],
'HARMONIC'            : ['EL-MA', 'ACOUSTIC', 'PIEZO'],
'SS-ROLLING'          : ['ROTATION A', 'CORNERING AXIS'],
'RESPONSE'            : ['SPECTRUM', 'DYNAMIC', 'MODAL INCREMENT', 'MODAL SHAPE', 'RESPONSE SPECTRUM', 'USSD subroutine'],
'R-P FLOW'            : ['PARAMETERS', 'UNEWTN subroutine', 'CONTROL'],
'SPFLOW'              : ['FOLLOW FOR', 'ISOTROPIC', 'SUPERPLASTIC'],
'LARGE DISP'          : [],
'LARGE STRAIN'        : ['MOONEY', 'OGDEN', 'GENT', 'ARRUDBOYCE', 'FOAM', 'ISOTROPIC', 'ORTHOTROPIC', 'ANISOTROPIC', 'NLELAST', 'HYPOELASTIC', 'SHAPE MEMORY', 'SOIL'],
'UPDATE'              : ['LARGE DISP'],
'FINITE'              : ['UPDATE'],
'CONSTANT DILATATION' : [],
'ASSUMED STRAIN'      : [],
'ELASTICITY'          : [],
'PLASTICITY'          : [],
'FOLLOW FOR'          : ['NO LOADCOR', 'FORCEM subroutine', 'DISP CHANGE', 'POINT LOAD', 'DIST LOADS', 'SOLVER'],
'BUCKLE'              : ['BUCKLE INCREMENT', 'RECOVER', 'LARGE DISP'],
'CREEP'               : ['CRPLAW subroutine', 'VSWELL subroutine', 'VISCO ELAS'],
'VISCO ELAS'          : ['CRPVIS subroutine', 'CREEP', 'VSWELL subroutine', 'CRPLAW subroutine'],
'STRUCTURAL'          : ['HEAT', 'JOULE', 'ELECTRO', 'MAGNETO', 'ACOUSTIC', 'PIEZO', 'FIXED DISP', 'POINT LOAD', 'DIST LOADS', 'FOUNDATION', 'CONTACT'],
'COUPLE'              : ['DIST FLUXES', 'CUPFLX subroutine', 'CONVERT', 'HEAT', 'JOULE'],
'DECOUPLING'          : ['READ FILE', 'WRITE FILE'],
'FLUID'               : ['PARAMETERS'],
'PORE'                : [],
'T-T-T'               : ['TIME-TEMP'],
'HEAT'                : ['FLUID', 'STRUCTURAL', 'JOULE', 'ELECTRO', 'MAGNETO', 'EL-MA'],
'JOULE'               : ['VOLTAGE', 'DIST CURRENT', 'POINT CURRENT', 'COUPLE', 'STRUCTURAL', 'CONTACT'],
'DIFFUSION'           : ['FIXED PRESSURE', 'DIST MASS', 'POINT MASS'],
'ABLATION'            : ['PYROLYSIS', 'RECEDING SURFACE', 'SURFACE ENERGY'],
'PYROLYSIS'           : ['THERMAL CONTACT', 'STREAM DEFINITION'],
'CURING'              : [],
'BEARING'             : ['VELOCITY', 'THICKNESS', 'RESTRICTOR', 'ISOTROPIC', 'FIXED PRESSURE', 'DAMPING COMPONENTS', 'STIFFNS COMPONENTS', 'THICKNS CHANGE'],
'ELECTRO'             : ['ISOTROPIC', 'ORTHOTROPIC', 'FIXED POTENTIAL', 'DIST CHARGES', 'POINT CHARGE', 'STEADY STATE', 'STRUCTURAL', 'HEAT'],
'MAGNETO'             : ['ISOTROPIC', 'ORTHOTROPIC', 'FIXED POTENTIAL', 'POINT CURRENT', 'DIST CURRENT', 'B-H RELATION', 'PERMANENT', 'STEADY STATE', 'STRUCTURAL', 'HEAT'],
'EL-MA'               : ['ISOTROPIC', 'ORTHOTROPIC', 'FIXED POTENTIAL', 'DIST CURRENT', 'POINT CURRENT-CHARGE', 'HARMONIC', 'DYNAMIC CHANGE', 'HEAT'],
'PIEZO'               : [],
'ACOUSTIC'            : ['FIXED PRESSURE', 'DIST SOURCES', 'POINT SOURCE', 'MODAL SHAPE', 'DYNAMIC CHANGE', 'CONTACT', 'HARMONIC', 'CONTACT TABLE'],
'RADIATION'           : ['PARAMETERS', 'RADIATING CAVITY', 'ISOTROPIC', 'ORTHOTROPIC', 'VIEW FACTOR', 'CAVITY DEFINITION', 'RAD-CAVITY', 'LOADCASE', 'EMISSIVITY', 'PARAMETERS', 'ABLATION'],
'CAVITY'              : ['FOLLOW FOR'],
'RBE'                 : ['RBE2', 'RBE3'],
'MACHINING'           : []}