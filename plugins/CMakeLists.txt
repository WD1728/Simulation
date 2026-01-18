
cmake_minimum_required(VERSION 2.8 FATAL_ERROR)

project(animated_box)

# Find packages

find_package(gazebo REQUIRED)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ${GAZEBO_CXX_FLAGS}")

# include appropriate directories
include_directories(${GAZEBO_INCLUDE_DIRS})
link_directories(${GAZEBO_LIBRARY_DIRS})

# Create libraries and executables

add_library(obs_0 SHARED obs_0.cc)
target_link_libraries(obs_0 ${GAZEBO_LIBRARIES})

add_library(obs_1 SHARED obs_1.cc)
target_link_libraries(obs_1 ${GAZEBO_LIBRARIES})

add_library(obs_2 SHARED obs_2.cc)
target_link_libraries(obs_2 ${GAZEBO_LIBRARIES})

add_library(obs_3 SHARED obs_3.cc)
target_link_libraries(obs_3 ${GAZEBO_LIBRARIES})

add_library(obs_4 SHARED obs_4.cc)
target_link_libraries(obs_4 ${GAZEBO_LIBRARIES})

add_library(obs_5 SHARED obs_5.cc)
target_link_libraries(obs_5 ${GAZEBO_LIBRARIES})

add_library(obs_6 SHARED obs_6.cc)
target_link_libraries(obs_6 ${GAZEBO_LIBRARIES})

add_library(obs_7 SHARED obs_7.cc)
target_link_libraries(obs_7 ${GAZEBO_LIBRARIES})

add_library(obs_8 SHARED obs_8.cc)
target_link_libraries(obs_8 ${GAZEBO_LIBRARIES})

add_library(obs_9 SHARED obs_9.cc)
target_link_libraries(obs_9 ${GAZEBO_LIBRARIES})

add_library(obs_10 SHARED obs_10.cc)
target_link_libraries(obs_10 ${GAZEBO_LIBRARIES})

add_library(obs_11 SHARED obs_11.cc)
target_link_libraries(obs_11 ${GAZEBO_LIBRARIES})

add_library(obs_12 SHARED obs_12.cc)
target_link_libraries(obs_12 ${GAZEBO_LIBRARIES})

add_library(obs_13 SHARED obs_13.cc)
target_link_libraries(obs_13 ${GAZEBO_LIBRARIES})

add_library(obs_14 SHARED obs_14.cc)
target_link_libraries(obs_14 ${GAZEBO_LIBRARIES})

add_library(obs_15 SHARED obs_15.cc)
target_link_libraries(obs_15 ${GAZEBO_LIBRARIES})

add_library(obs_16 SHARED obs_16.cc)
target_link_libraries(obs_16 ${GAZEBO_LIBRARIES})

add_library(obs_17 SHARED obs_17.cc)
target_link_libraries(obs_17 ${GAZEBO_LIBRARIES})

add_library(obs_18 SHARED obs_18.cc)
target_link_libraries(obs_18 ${GAZEBO_LIBRARIES})

add_library(obs_19 SHARED obs_19.cc)
target_link_libraries(obs_19 ${GAZEBO_LIBRARIES})

add_library(obs_20 SHARED obs_20.cc)
target_link_libraries(obs_20 ${GAZEBO_LIBRARIES})

add_library(obs_21 SHARED obs_21.cc)
target_link_libraries(obs_21 ${GAZEBO_LIBRARIES})

add_library(obs_22 SHARED obs_22.cc)
target_link_libraries(obs_22 ${GAZEBO_LIBRARIES})

add_library(obs_23 SHARED obs_23.cc)
target_link_libraries(obs_23 ${GAZEBO_LIBRARIES})

add_library(obs_24 SHARED obs_24.cc)
target_link_libraries(obs_24 ${GAZEBO_LIBRARIES})

add_library(obs_25 SHARED obs_25.cc)
target_link_libraries(obs_25 ${GAZEBO_LIBRARIES})

add_library(obs_26 SHARED obs_26.cc)
target_link_libraries(obs_26 ${GAZEBO_LIBRARIES})

add_library(obs_27 SHARED obs_27.cc)
target_link_libraries(obs_27 ${GAZEBO_LIBRARIES})

add_library(obs_28 SHARED obs_28.cc)
target_link_libraries(obs_28 ${GAZEBO_LIBRARIES})

add_library(obs_29 SHARED obs_29.cc)
target_link_libraries(obs_29 ${GAZEBO_LIBRARIES})

add_library(obs_30 SHARED obs_30.cc)
target_link_libraries(obs_30 ${GAZEBO_LIBRARIES})

add_library(obs_31 SHARED obs_31.cc)
target_link_libraries(obs_31 ${GAZEBO_LIBRARIES})

add_library(obs_32 SHARED obs_32.cc)
target_link_libraries(obs_32 ${GAZEBO_LIBRARIES})

add_library(obs_33 SHARED obs_33.cc)
target_link_libraries(obs_33 ${GAZEBO_LIBRARIES})

add_library(obs_34 SHARED obs_34.cc)
target_link_libraries(obs_34 ${GAZEBO_LIBRARIES})

add_library(obs_35 SHARED obs_35.cc)
target_link_libraries(obs_35 ${GAZEBO_LIBRARIES})

add_library(obs_36 SHARED obs_36.cc)
target_link_libraries(obs_36 ${GAZEBO_LIBRARIES})

add_library(obs_37 SHARED obs_37.cc)
target_link_libraries(obs_37 ${GAZEBO_LIBRARIES})

add_library(obs_38 SHARED obs_38.cc)
target_link_libraries(obs_38 ${GAZEBO_LIBRARIES})

add_library(obs_39 SHARED obs_39.cc)
target_link_libraries(obs_39 ${GAZEBO_LIBRARIES})

add_library(obs_40 SHARED obs_40.cc)
target_link_libraries(obs_40 ${GAZEBO_LIBRARIES})

add_library(obs_41 SHARED obs_41.cc)
target_link_libraries(obs_41 ${GAZEBO_LIBRARIES})

add_library(obs_42 SHARED obs_42.cc)
target_link_libraries(obs_42 ${GAZEBO_LIBRARIES})

add_library(obs_43 SHARED obs_43.cc)
target_link_libraries(obs_43 ${GAZEBO_LIBRARIES})

add_library(obs_44 SHARED obs_44.cc)
target_link_libraries(obs_44 ${GAZEBO_LIBRARIES})

add_library(obs_45 SHARED obs_45.cc)
target_link_libraries(obs_45 ${GAZEBO_LIBRARIES})

add_library(obs_46 SHARED obs_46.cc)
target_link_libraries(obs_46 ${GAZEBO_LIBRARIES})

add_library(obs_47 SHARED obs_47.cc)
target_link_libraries(obs_47 ${GAZEBO_LIBRARIES})

add_library(obs_48 SHARED obs_48.cc)
target_link_libraries(obs_48 ${GAZEBO_LIBRARIES})

add_library(obs_49 SHARED obs_49.cc)
target_link_libraries(obs_49 ${GAZEBO_LIBRARIES})

add_library(obs_50 SHARED obs_50.cc)
target_link_libraries(obs_50 ${GAZEBO_LIBRARIES})

add_library(obs_51 SHARED obs_51.cc)
target_link_libraries(obs_51 ${GAZEBO_LIBRARIES})

add_library(obs_52 SHARED obs_52.cc)
target_link_libraries(obs_52 ${GAZEBO_LIBRARIES})

add_library(obs_53 SHARED obs_53.cc)
target_link_libraries(obs_53 ${GAZEBO_LIBRARIES})

add_library(obs_54 SHARED obs_54.cc)
target_link_libraries(obs_54 ${GAZEBO_LIBRARIES})

add_library(obs_55 SHARED obs_55.cc)
target_link_libraries(obs_55 ${GAZEBO_LIBRARIES})

add_library(obs_56 SHARED obs_56.cc)
target_link_libraries(obs_56 ${GAZEBO_LIBRARIES})

add_library(obs_57 SHARED obs_57.cc)
target_link_libraries(obs_57 ${GAZEBO_LIBRARIES})

add_library(obs_58 SHARED obs_58.cc)
target_link_libraries(obs_58 ${GAZEBO_LIBRARIES})

add_library(obs_59 SHARED obs_59.cc)
target_link_libraries(obs_59 ${GAZEBO_LIBRARIES})

add_library(obs_60 SHARED obs_60.cc)
target_link_libraries(obs_60 ${GAZEBO_LIBRARIES})

add_library(obs_61 SHARED obs_61.cc)
target_link_libraries(obs_61 ${GAZEBO_LIBRARIES})

add_library(obs_62 SHARED obs_62.cc)
target_link_libraries(obs_62 ${GAZEBO_LIBRARIES})

add_library(obs_63 SHARED obs_63.cc)
target_link_libraries(obs_63 ${GAZEBO_LIBRARIES})

add_library(obs_64 SHARED obs_64.cc)
target_link_libraries(obs_64 ${GAZEBO_LIBRARIES})

add_library(obs_65 SHARED obs_65.cc)
target_link_libraries(obs_65 ${GAZEBO_LIBRARIES})

add_library(obs_66 SHARED obs_66.cc)
target_link_libraries(obs_66 ${GAZEBO_LIBRARIES})

add_library(obs_67 SHARED obs_67.cc)
target_link_libraries(obs_67 ${GAZEBO_LIBRARIES})

add_library(obs_68 SHARED obs_68.cc)
target_link_libraries(obs_68 ${GAZEBO_LIBRARIES})

add_library(obs_69 SHARED obs_69.cc)
target_link_libraries(obs_69 ${GAZEBO_LIBRARIES})

add_library(obs_70 SHARED obs_70.cc)
target_link_libraries(obs_70 ${GAZEBO_LIBRARIES})

add_library(obs_71 SHARED obs_71.cc)
target_link_libraries(obs_71 ${GAZEBO_LIBRARIES})

add_library(obs_72 SHARED obs_72.cc)
target_link_libraries(obs_72 ${GAZEBO_LIBRARIES})

add_library(obs_73 SHARED obs_73.cc)
target_link_libraries(obs_73 ${GAZEBO_LIBRARIES})

add_library(obs_74 SHARED obs_74.cc)
target_link_libraries(obs_74 ${GAZEBO_LIBRARIES})

add_library(obs_75 SHARED obs_75.cc)
target_link_libraries(obs_75 ${GAZEBO_LIBRARIES})

add_library(obs_76 SHARED obs_76.cc)
target_link_libraries(obs_76 ${GAZEBO_LIBRARIES})

add_library(obs_77 SHARED obs_77.cc)
target_link_libraries(obs_77 ${GAZEBO_LIBRARIES})

add_library(obs_78 SHARED obs_78.cc)
target_link_libraries(obs_78 ${GAZEBO_LIBRARIES})

add_library(obs_79 SHARED obs_79.cc)
target_link_libraries(obs_79 ${GAZEBO_LIBRARIES})

add_library(obs_80 SHARED obs_80.cc)
target_link_libraries(obs_80 ${GAZEBO_LIBRARIES})

add_library(obs_81 SHARED obs_81.cc)
target_link_libraries(obs_81 ${GAZEBO_LIBRARIES})

add_library(obs_82 SHARED obs_82.cc)
target_link_libraries(obs_82 ${GAZEBO_LIBRARIES})

add_library(obs_83 SHARED obs_83.cc)
target_link_libraries(obs_83 ${GAZEBO_LIBRARIES})

add_library(obs_84 SHARED obs_84.cc)
target_link_libraries(obs_84 ${GAZEBO_LIBRARIES})

add_library(obs_85 SHARED obs_85.cc)
target_link_libraries(obs_85 ${GAZEBO_LIBRARIES})

add_library(obs_86 SHARED obs_86.cc)
target_link_libraries(obs_86 ${GAZEBO_LIBRARIES})

add_library(obs_87 SHARED obs_87.cc)
target_link_libraries(obs_87 ${GAZEBO_LIBRARIES})

add_library(obs_88 SHARED obs_88.cc)
target_link_libraries(obs_88 ${GAZEBO_LIBRARIES})

add_library(obs_89 SHARED obs_89.cc)
target_link_libraries(obs_89 ${GAZEBO_LIBRARIES})

add_library(obs_90 SHARED obs_90.cc)
target_link_libraries(obs_90 ${GAZEBO_LIBRARIES})

add_library(obs_91 SHARED obs_91.cc)
target_link_libraries(obs_91 ${GAZEBO_LIBRARIES})

add_library(obs_92 SHARED obs_92.cc)
target_link_libraries(obs_92 ${GAZEBO_LIBRARIES})

add_library(obs_93 SHARED obs_93.cc)
target_link_libraries(obs_93 ${GAZEBO_LIBRARIES})

add_library(obs_94 SHARED obs_94.cc)
target_link_libraries(obs_94 ${GAZEBO_LIBRARIES})

add_library(obs_95 SHARED obs_95.cc)
target_link_libraries(obs_95 ${GAZEBO_LIBRARIES})

add_library(obs_96 SHARED obs_96.cc)
target_link_libraries(obs_96 ${GAZEBO_LIBRARIES})

add_library(obs_97 SHARED obs_97.cc)
target_link_libraries(obs_97 ${GAZEBO_LIBRARIES})

add_library(obs_98 SHARED obs_98.cc)
target_link_libraries(obs_98 ${GAZEBO_LIBRARIES})

add_library(obs_99 SHARED obs_99.cc)
target_link_libraries(obs_99 ${GAZEBO_LIBRARIES})

add_library(obs_100 SHARED obs_100.cc)
target_link_libraries(obs_100 ${GAZEBO_LIBRARIES})

add_library(obs_101 SHARED obs_101.cc)
target_link_libraries(obs_101 ${GAZEBO_LIBRARIES})

add_library(obs_102 SHARED obs_102.cc)
target_link_libraries(obs_102 ${GAZEBO_LIBRARIES})

add_library(obs_103 SHARED obs_103.cc)
target_link_libraries(obs_103 ${GAZEBO_LIBRARIES})

add_library(obs_104 SHARED obs_104.cc)
target_link_libraries(obs_104 ${GAZEBO_LIBRARIES})

add_library(obs_105 SHARED obs_105.cc)
target_link_libraries(obs_105 ${GAZEBO_LIBRARIES})

add_library(obs_106 SHARED obs_106.cc)
target_link_libraries(obs_106 ${GAZEBO_LIBRARIES})

add_library(obs_107 SHARED obs_107.cc)
target_link_libraries(obs_107 ${GAZEBO_LIBRARIES})

add_library(obs_108 SHARED obs_108.cc)
target_link_libraries(obs_108 ${GAZEBO_LIBRARIES})

add_library(obs_109 SHARED obs_109.cc)
target_link_libraries(obs_109 ${GAZEBO_LIBRARIES})

add_library(obs_110 SHARED obs_110.cc)
target_link_libraries(obs_110 ${GAZEBO_LIBRARIES})

add_library(obs_111 SHARED obs_111.cc)
target_link_libraries(obs_111 ${GAZEBO_LIBRARIES})

add_library(obs_112 SHARED obs_112.cc)
target_link_libraries(obs_112 ${GAZEBO_LIBRARIES})

add_library(obs_113 SHARED obs_113.cc)
target_link_libraries(obs_113 ${GAZEBO_LIBRARIES})

add_library(obs_114 SHARED obs_114.cc)
target_link_libraries(obs_114 ${GAZEBO_LIBRARIES})

add_library(obs_115 SHARED obs_115.cc)
target_link_libraries(obs_115 ${GAZEBO_LIBRARIES})

add_library(obs_116 SHARED obs_116.cc)
target_link_libraries(obs_116 ${GAZEBO_LIBRARIES})

add_library(obs_117 SHARED obs_117.cc)
target_link_libraries(obs_117 ${GAZEBO_LIBRARIES})

add_library(obs_118 SHARED obs_118.cc)
target_link_libraries(obs_118 ${GAZEBO_LIBRARIES})

add_library(obs_119 SHARED obs_119.cc)
target_link_libraries(obs_119 ${GAZEBO_LIBRARIES})

add_library(obs_120 SHARED obs_120.cc)
target_link_libraries(obs_120 ${GAZEBO_LIBRARIES})

add_library(obs_121 SHARED obs_121.cc)
target_link_libraries(obs_121 ${GAZEBO_LIBRARIES})

add_library(obs_122 SHARED obs_122.cc)
target_link_libraries(obs_122 ${GAZEBO_LIBRARIES})

add_library(obs_123 SHARED obs_123.cc)
target_link_libraries(obs_123 ${GAZEBO_LIBRARIES})

add_library(obs_124 SHARED obs_124.cc)
target_link_libraries(obs_124 ${GAZEBO_LIBRARIES})

add_library(obs_125 SHARED obs_125.cc)
target_link_libraries(obs_125 ${GAZEBO_LIBRARIES})

add_library(obs_126 SHARED obs_126.cc)
target_link_libraries(obs_126 ${GAZEBO_LIBRARIES})

add_library(obs_127 SHARED obs_127.cc)
target_link_libraries(obs_127 ${GAZEBO_LIBRARIES})

add_library(obs_128 SHARED obs_128.cc)
target_link_libraries(obs_128 ${GAZEBO_LIBRARIES})

add_library(obs_129 SHARED obs_129.cc)
target_link_libraries(obs_129 ${GAZEBO_LIBRARIES})

add_library(obs_130 SHARED obs_130.cc)
target_link_libraries(obs_130 ${GAZEBO_LIBRARIES})

add_library(obs_131 SHARED obs_131.cc)
target_link_libraries(obs_131 ${GAZEBO_LIBRARIES})

add_library(obs_132 SHARED obs_132.cc)
target_link_libraries(obs_132 ${GAZEBO_LIBRARIES})

add_library(obs_133 SHARED obs_133.cc)
target_link_libraries(obs_133 ${GAZEBO_LIBRARIES})

add_library(obs_134 SHARED obs_134.cc)
target_link_libraries(obs_134 ${GAZEBO_LIBRARIES})

add_library(obs_135 SHARED obs_135.cc)
target_link_libraries(obs_135 ${GAZEBO_LIBRARIES})

add_library(obs_136 SHARED obs_136.cc)
target_link_libraries(obs_136 ${GAZEBO_LIBRARIES})

add_library(obs_137 SHARED obs_137.cc)
target_link_libraries(obs_137 ${GAZEBO_LIBRARIES})

add_library(obs_138 SHARED obs_138.cc)
target_link_libraries(obs_138 ${GAZEBO_LIBRARIES})

add_library(obs_139 SHARED obs_139.cc)
target_link_libraries(obs_139 ${GAZEBO_LIBRARIES})

add_library(obs_140 SHARED obs_140.cc)
target_link_libraries(obs_140 ${GAZEBO_LIBRARIES})

add_library(obs_141 SHARED obs_141.cc)
target_link_libraries(obs_141 ${GAZEBO_LIBRARIES})

add_library(obs_142 SHARED obs_142.cc)
target_link_libraries(obs_142 ${GAZEBO_LIBRARIES})

add_library(obs_143 SHARED obs_143.cc)
target_link_libraries(obs_143 ${GAZEBO_LIBRARIES})

add_library(obs_144 SHARED obs_144.cc)
target_link_libraries(obs_144 ${GAZEBO_LIBRARIES})

add_library(obs_145 SHARED obs_145.cc)
target_link_libraries(obs_145 ${GAZEBO_LIBRARIES})

add_library(obs_146 SHARED obs_146.cc)
target_link_libraries(obs_146 ${GAZEBO_LIBRARIES})

add_library(obs_147 SHARED obs_147.cc)
target_link_libraries(obs_147 ${GAZEBO_LIBRARIES})

add_library(obs_148 SHARED obs_148.cc)
target_link_libraries(obs_148 ${GAZEBO_LIBRARIES})

add_library(obs_149 SHARED obs_149.cc)
target_link_libraries(obs_149 ${GAZEBO_LIBRARIES})

add_library(obs_150 SHARED obs_150.cc)
target_link_libraries(obs_150 ${GAZEBO_LIBRARIES})

add_library(obs_151 SHARED obs_151.cc)
target_link_libraries(obs_151 ${GAZEBO_LIBRARIES})

add_library(obs_152 SHARED obs_152.cc)
target_link_libraries(obs_152 ${GAZEBO_LIBRARIES})

add_library(obs_153 SHARED obs_153.cc)
target_link_libraries(obs_153 ${GAZEBO_LIBRARIES})

add_library(obs_154 SHARED obs_154.cc)
target_link_libraries(obs_154 ${GAZEBO_LIBRARIES})

add_library(obs_155 SHARED obs_155.cc)
target_link_libraries(obs_155 ${GAZEBO_LIBRARIES})

add_library(obs_156 SHARED obs_156.cc)
target_link_libraries(obs_156 ${GAZEBO_LIBRARIES})

add_library(obs_157 SHARED obs_157.cc)
target_link_libraries(obs_157 ${GAZEBO_LIBRARIES})

add_library(obs_158 SHARED obs_158.cc)
target_link_libraries(obs_158 ${GAZEBO_LIBRARIES})

add_library(obs_159 SHARED obs_159.cc)
target_link_libraries(obs_159 ${GAZEBO_LIBRARIES})

add_library(obs_160 SHARED obs_160.cc)
target_link_libraries(obs_160 ${GAZEBO_LIBRARIES})

add_library(obs_161 SHARED obs_161.cc)
target_link_libraries(obs_161 ${GAZEBO_LIBRARIES})

add_library(obs_162 SHARED obs_162.cc)
target_link_libraries(obs_162 ${GAZEBO_LIBRARIES})

add_library(obs_163 SHARED obs_163.cc)
target_link_libraries(obs_163 ${GAZEBO_LIBRARIES})

add_library(obs_164 SHARED obs_164.cc)
target_link_libraries(obs_164 ${GAZEBO_LIBRARIES})

add_library(obs_165 SHARED obs_165.cc)
target_link_libraries(obs_165 ${GAZEBO_LIBRARIES})

add_library(obs_166 SHARED obs_166.cc)
target_link_libraries(obs_166 ${GAZEBO_LIBRARIES})

add_library(obs_167 SHARED obs_167.cc)
target_link_libraries(obs_167 ${GAZEBO_LIBRARIES})

add_library(obs_168 SHARED obs_168.cc)
target_link_libraries(obs_168 ${GAZEBO_LIBRARIES})

add_library(obs_169 SHARED obs_169.cc)
target_link_libraries(obs_169 ${GAZEBO_LIBRARIES})

add_library(obs_170 SHARED obs_170.cc)
target_link_libraries(obs_170 ${GAZEBO_LIBRARIES})

add_library(obs_171 SHARED obs_171.cc)
target_link_libraries(obs_171 ${GAZEBO_LIBRARIES})

add_library(obs_172 SHARED obs_172.cc)
target_link_libraries(obs_172 ${GAZEBO_LIBRARIES})

add_library(obs_173 SHARED obs_173.cc)
target_link_libraries(obs_173 ${GAZEBO_LIBRARIES})

add_library(obs_174 SHARED obs_174.cc)
target_link_libraries(obs_174 ${GAZEBO_LIBRARIES})

add_library(obs_175 SHARED obs_175.cc)
target_link_libraries(obs_175 ${GAZEBO_LIBRARIES})

add_library(obs_176 SHARED obs_176.cc)
target_link_libraries(obs_176 ${GAZEBO_LIBRARIES})

add_library(obs_177 SHARED obs_177.cc)
target_link_libraries(obs_177 ${GAZEBO_LIBRARIES})

add_library(obs_178 SHARED obs_178.cc)
target_link_libraries(obs_178 ${GAZEBO_LIBRARIES})

add_library(obs_179 SHARED obs_179.cc)
target_link_libraries(obs_179 ${GAZEBO_LIBRARIES})

add_library(obs_180 SHARED obs_180.cc)
target_link_libraries(obs_180 ${GAZEBO_LIBRARIES})

add_library(obs_181 SHARED obs_181.cc)
target_link_libraries(obs_181 ${GAZEBO_LIBRARIES})

add_library(obs_182 SHARED obs_182.cc)
target_link_libraries(obs_182 ${GAZEBO_LIBRARIES})

add_library(obs_183 SHARED obs_183.cc)
target_link_libraries(obs_183 ${GAZEBO_LIBRARIES})

add_library(obs_184 SHARED obs_184.cc)
target_link_libraries(obs_184 ${GAZEBO_LIBRARIES})

add_library(obs_185 SHARED obs_185.cc)
target_link_libraries(obs_185 ${GAZEBO_LIBRARIES})

add_library(obs_186 SHARED obs_186.cc)
target_link_libraries(obs_186 ${GAZEBO_LIBRARIES})

add_library(obs_187 SHARED obs_187.cc)
target_link_libraries(obs_187 ${GAZEBO_LIBRARIES})

add_library(obs_188 SHARED obs_188.cc)
target_link_libraries(obs_188 ${GAZEBO_LIBRARIES})

add_library(obs_189 SHARED obs_189.cc)
target_link_libraries(obs_189 ${GAZEBO_LIBRARIES})

add_library(obs_190 SHARED obs_190.cc)
target_link_libraries(obs_190 ${GAZEBO_LIBRARIES})

add_library(obs_191 SHARED obs_191.cc)
target_link_libraries(obs_191 ${GAZEBO_LIBRARIES})

add_library(obs_192 SHARED obs_192.cc)
target_link_libraries(obs_192 ${GAZEBO_LIBRARIES})

add_library(obs_193 SHARED obs_193.cc)
target_link_libraries(obs_193 ${GAZEBO_LIBRARIES})

add_library(obs_194 SHARED obs_194.cc)
target_link_libraries(obs_194 ${GAZEBO_LIBRARIES})

add_library(obs_195 SHARED obs_195.cc)
target_link_libraries(obs_195 ${GAZEBO_LIBRARIES})

add_library(obs_196 SHARED obs_196.cc)
target_link_libraries(obs_196 ${GAZEBO_LIBRARIES})

add_library(obs_197 SHARED obs_197.cc)
target_link_libraries(obs_197 ${GAZEBO_LIBRARIES})

add_library(obs_198 SHARED obs_198.cc)
target_link_libraries(obs_198 ${GAZEBO_LIBRARIES})

add_library(obs_199 SHARED obs_199.cc)
target_link_libraries(obs_199 ${GAZEBO_LIBRARIES})
